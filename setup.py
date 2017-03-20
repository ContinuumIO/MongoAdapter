import os
import sys
from distutils.core import setup, Command
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
import versioneer


class CleanInplace(Command):
    user_options = []

    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        files = ['./mongoadapter/core/MongoAdapter.c',
                 './mongoadapter/core/MongoAdapter.so']
        for file in files:
            try:
                os.remove(file)
            except OSError:
                pass


def setup_mongo(include_dirs, lib_dirs):
    src = ['mongoadapter/core/MongoAdapter.pyx',
           'mongoadapter/core/mongo_adapter.c',
           'mongoadapter/lib/field_info.c',
           'mongoadapter/lib/converter_functions.c']

    return Extension("mongoadapter.core.MongoAdapter",
                     src,
                     include_dirs=include_dirs,
                     libraries=['mongoc', 'bson'],
                     library_dirs=lib_dirs)


def run_setup():

    include_dirs = [os.path.join('mongoadapter', 'lib'),
                    numpy.get_include()]
    if sys.platform == 'win32':
        include_dirs.append(os.path.join(sys.prefix, 'Library', 'include'))
    else:
        include_dirs.append(os.path.join(sys.prefix, 'include'))

    lib_dirs = []
    if sys.platform == 'win32':
        lib_dirs.append(os.path.join(sys.prefix, 'Library', 'lib'))
    else:
        lib_dirs.append(os.path.join(sys.prefix, 'lib'))

    ext_modules = []
    packages = ['mongoadapter', 'mongoadapter.lib', 'mongoadapter.tests']
    ext_modules.append(setup_mongo(include_dirs, lib_dirs))
    packages.append('mongoadapter.core')

    versioneer.versionfile_source = 'mongoadapter/_version.py'
    versioneer.versionfile_build = 'mongoadapter/_version.py'
    versioneer.tag_prefix = ''
    versioneer.parentdir_prefix = 'mongoadapter-'

    cmdclass = versioneer.get_cmdclass()
    cmdclass['build_ext'] = build_ext
    cmdclass['cleanall'] = CleanInplace

    setup(name='mongoadapter',
          version = versioneer.get_version(),
          description='optimized IO for NumPy/Blaze',
          author='Continuum Analytics',
          author_email='support@continuum.io',
          ext_modules=ext_modules,
          packages=packages,
          cmdclass=cmdclass)


if __name__ == '__main__':
    run_setup()
