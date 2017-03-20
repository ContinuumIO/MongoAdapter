"""
    MongoAdapter
    ~~~~~~~~~~~~

    MongoAdapter provides tools to interface Mongo databases in a fast,
    memory-efficient way.
"""
from __future__ import absolute_import

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

from mongoadapter.lib.errors import (AdapterException, AdapterIndexError,
                                     ArgumentError, ConfigurationError,
                                     DataIndexError, DataTypeError,
                                     InternalInconsistencyError, NoSuchFieldError,
                                     ParserError, SourceError, SourceNotFoundError)

from mongoadapter.core.MongoAdapter import (MongoAdapter, MongoAdapterFields,
                                            dtype_converter_mapping)


def test(host='localhost', port=27017, verbosity=2):
    from .tests.test_MongoAdapter import run as run_mongo_tests
    result = run_mongo_tests(verbosity, host, port)
    if result is None or not result.wasSuccessful():
        return False
    return True

