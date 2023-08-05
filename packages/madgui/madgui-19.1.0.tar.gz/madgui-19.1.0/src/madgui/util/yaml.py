import sys
from collections import OrderedDict

import numpy as np
import yaml


# Let's not define bare `load`, `safe` for now:
__all__ = [
    'load_file',
    'safe_load',
    'safe_dump',
    'YAMLError',
    'ParserError',
    'ScannerError',
]

# For speed:
SafeLoader = getattr(yaml, 'CSafeLoader', yaml.SafeLoader)
SafeDumper = getattr(yaml, 'CSafeDumper', yaml.SafeDumper)

YAMLError = yaml.error.YAMLError
ParserError = yaml.parser.ParserError
ScannerError = yaml.scanner.ScannerError


def load_file(filename):
    """Load yaml document from filename."""
    with open(filename, 'rb') as f:
        return safe_load(f)


if sys.version_info >= (3, 6):
    def safe_load(stream, Loader=SafeLoader):
        return yaml.load(stream, Loader)

else:
    def safe_load(stream, Loader=SafeLoader):
        class OrderedLoader(Loader):
            pass

        def construct_mapping(loader, node):
            loader.flatten_mapping(node)
            return OrderedDict(loader.construct_pairs(node))
        OrderedLoader.add_constructor(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            construct_mapping)
        return yaml.load(stream, OrderedLoader)


def safe_dump(data, stream=None, Dumper=SafeDumper, **kwds):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    OrderedDumper.add_representer(np.bool, Dumper.represent_bool)
    OrderedDumper.add_representer(np.int32, Dumper.represent_int)
    OrderedDumper.add_representer(np.int64, Dumper.represent_int)
    OrderedDumper.add_representer(np.float32, Dumper.represent_float)
    OrderedDumper.add_representer(np.float64, Dumper.represent_float)
    return yaml.dump(data, stream, OrderedDumper, **kwds)
