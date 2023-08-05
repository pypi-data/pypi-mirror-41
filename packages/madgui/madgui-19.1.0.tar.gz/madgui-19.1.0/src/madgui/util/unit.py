"""
Provides unit conversion.
"""

__all__ = [
    'units',
    'strip_unit',
    'tounit',
    'format_quantity',
    'get_raw_label',
    'from_config',
    'UnitConverter',
]

from numbers import Number
from importlib_resources import read_binary

import numpy as np
import pint
import yaml

from madgui.util.defaultdict import DefaultDict


units = pint.UnitRegistry(on_redefinition='ignore')
units.default_format = 'P~'     # make `str(quantity)` slightly nicer
units.define('ratio = []')
units.define('percent = 0.01 ratio = %')
units.define('permille = 0.001 ratio = ‰')
units.define('degree = pi / 180 * radian = °'
             '= deg = arcdeg = arcdegree = angular_degree')


number_types = (int, float, units.Quantity)


def get_unit(quantity):
    if isinstance(quantity, units.Quantity):
        return units.Quantity(1, quantity.units)
    return None


def add_unit(quantity, unit):
    if quantity is None or unit is None:
        return quantity
    if isinstance(quantity, units.Quantity):
        return quantity.to(toquantity(unit))
    return quantity * unit


def strip_unit(quantity, unit=None):
    """Convert the quantity to a plain float."""
    if quantity is None:
        return None
    if unit is None:
        try:
            return quantity.magnitude
        except AttributeError:
            return quantity
    if isinstance(unit, (list, tuple)):
        # FIXME: 'zip' truncates without warning if not enough units
        # are defined
        return [q.to(u).magnitude for q, u in zip(quantity, unit)]
    try:
        return quantity.to(unit).magnitude
    except AttributeError:
        return quantity


def change_unit(quantity, from_unit, to_unit):
    return strip_unit(
        add_unit(quantity, from_config(from_unit)), from_config(to_unit))


def toquantity(value):
    if value is None:
        return None
    if isinstance(value, units.Quantity):
        return value
    return units.Quantity(value)


def tounit(quantity, unit):
    """Cast the quantity to a specific unit."""
    if quantity is None:
        return None
    if unit is None:
        unit = 1
    return toquantity(quantity).to(toquantity(unit))


def format_quantity(quantity, num_spec=''):
    """Get a nice display string for the quantity."""
    num_fmt = '{:' + num_spec + '}'
    if isinstance(quantity, units.Quantity):
        magn = num_fmt.format(quantity.magnitude)
        unit = get_raw_label(quantity)
        return magn + ' ' + unit
    else:
        return num_fmt.format(quantity)


def get_raw_label(quantity):
    """Get the name of the unit, without enclosing brackets."""
    if quantity is None:
        return ''
    if isinstance(quantity, list):
        return '[{}]'.format(', '.join(map(get_raw_label, quantity)))
    quantity = from_config(quantity)
    if not isinstance(quantity, units.Quantity):
        return ''
    short = pint.unit.UnitsContainer(
        {units._get_symbol(key): value
         for key, value in quantity.units._units.items()})
    as_ratio = any(exp > 0 for _, exp in short.items())
    return pint.formatting.formatter(
        short.items(),
        as_ratio=as_ratio,
        single_denominator=True,
        product_fmt='·',
        division_fmt='/',
        power_fmt='{0}{1}',
        parentheses_fmt='({0})',
        exp_call=pint.formatting._pretty_fmt_exponent,
    )


def from_config(unit):
    """
    Parse a config entry for a unit to a :class:`pint.unit.Quantity` instance.

    The pint parser is quite powerful. Valid examples are:

        s / m²
        microsecond
        10 rad
        m^-2
    """
    if isinstance(unit, (units.Unit, units.Quantity, float, int)):
        return unit
    if not unit:
        return None
    if isinstance(unit, list):
        return [from_config(u) for u in unit]
    if isinstance(unit, bytes):
        unit = unit.decode('utf-8')
    unit = '{}'.format(unit)
    # as of pint-0.8.1 the following symbols fail to be parsed:
    unit = unit.replace('%', 'percent')
    unit = unit.replace('‰', 'permille')
    return units(unit)


class UnitConverter:

    """
    Quantity converter.

    Used to add and remove units from quanitities and evaluate expressions.

    :ivar dict _units: unit dictionary
    """

    def __init__(self, units):
        self._units = units

    @classmethod
    def from_config_dict(cls, conf_dict):
        """Convert a config dict of units to their in-memory representation."""
        return cls(DefaultDict(lambda k: from_config(conf_dict[k.lower()])))

    def get(self, name):
        return self._units.get(name)

    def label(self, name, value=None):
        """Get the name of the unit for the specified parameter name."""
        unit = self.get(name)
        if unit is None or value is None:
            return get_raw_label(unit)
        return get_raw_label(self._add_unit(value, unit))

    def add_unit(self, name, value):
        """Add units to a single number."""
        unit = self._units.get(name) if isinstance(name, str) else name
        if unit:
            if isinstance(value, (list, tuple)):
                # FIXME: 'zip' truncates without warning if not enough units
                # are defined
                return [self._add_unit(v, u)
                        for v, u in zip(value, unit)]
            return self._add_unit(value, unit)
        else:
            return value

    def _add_unit(self, value, unit):
        if value is None or unit is None:
            return value
        elif isinstance(unit, list):
            return [self._add_unit(v, u) for v, u in zip(value, unit)]
        elif isinstance(value, units.Quantity):
            return tounit(value, unit)
        elif isinstance(value, (Number, np.ndarray)):
            return unit * value
        else:
            return value

    def strip_unit(self, name, value):
        """Convert to MAD-X units."""
        unit = self._units.get(name) if isinstance(name, str) else name
        return strip_unit(value, unit)

    def dict_add_unit(self, obj):
        """Add units to all elements in a dictionary."""
        return obj.__class__((k, self.add_unit(k, obj[k])) for k in obj)

    def dict_strip_unit(self, obj):
        """Remove units from all elements in a dictionary."""
        return obj.__class__((k, self.strip_unit(k, obj[k])) for k in obj)


madx_units = UnitConverter.from_config_dict(yaml.safe_load(
    read_binary('madgui.data', 'madx_units.yml')))

ui_units = UnitConverter.from_config_dict(yaml.safe_load(
    read_binary('madgui.data', 'ui_units.yml')))


def convert(from_, to, *args):
    if len(args) == 1:
        return to.dict_strip_unit(from_.dict_add_unit(*args))
    if len(args) == 2:
        return to.strip_unit(args[0], from_.add_unit(*args))
    if len(args) == 3:
        return to.strip_unit(args[0], from_.add_unit(*args[1:]))
    raise TypeError("convert can only be called with one or two arguments.")


def from_ui(*args):
    return convert(ui_units, madx_units, *args)


def to_ui(*args):
    return convert(madx_units, ui_units, *args)
