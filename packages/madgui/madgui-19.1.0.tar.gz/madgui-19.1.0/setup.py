#!/usr/bin/env python
"""
Installation script for madgui.

Usage:
    python setup.py install
"""

import sys
from setuptools import setup, find_packages
from distutils.util import convert_path


def read_file(path):
    """Read a file in binary mode."""
    with open(convert_path(path), 'rb') as f:
        return f.read()


def exec_file(path):
    """Execute a python file and return the `globals` dictionary."""
    namespace = {}
    exec(read_file(path), namespace, namespace)
    return namespace


def get_long_description():
    """Compose a long description for PyPI."""
    long_description = None
    try:
        long_description = read_file('README.rst').decode('utf-8')
        long_description += '\n' + read_file('COPYING.rst').decode('utf-8')
        long_description += '\n' + read_file('CHANGES.rst').decode('utf-8')
    except (IOError, UnicodeDecodeError):
        pass
    return long_description


def main():
    """Execute setup."""
    long_description = get_long_description()
    meta = exec_file('src/madgui/__init__.py')
    mpl_version = '==2' if sys.version_info < (3, 5) else ''
    setup(
        name='madgui',
        version=meta['__version__'],
        description=meta['__summary__'],
        long_description=long_description,
        author=meta['__author__'],
        author_email=meta['__email__'],
        url=meta['__uri__'],
        license=meta['__license__'],
        classifiers=meta['__classifiers__'],
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=[
            'cpymad>=1.0.11',
            'docopt',           # command line parsing
            'matplotlib' + mpl_version,
            'numpy',
            'scipy',
            'PyYAML',           # config/model files
            'Pint==0.8.1',
            'docutils',         # about dialogs
            'pandas',           # optional cpymad dependency, used in orm
            # inprocess python shell:
            'ipython',
            'qtconsole',
            # 'PyQt5',
            'importlib_resources>=0.3',     # = importlib.resources in 3.7!
        ],
        entry_points="""
            [console_scripts]
            madgui = madgui.core.app:main
        """,
        include_package_data=True,  # install files matched by MANIFEST.in
    )


if __name__ == '__main__':
    main()
