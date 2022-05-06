import contextlib
from glob import glob
from distutils.core import setup

from distutils.command.build import build
import os

@contextlib.contextmanager
def changed_dir(dirname):
    oldcwd = os.getcwd()
    os.chdir(dirname)
    try:
        yield
    finally:
        os.chdir(oldcwd)

class cmake_then_build(build):
    def run(self):
        print("RUNNING BUILD CMD")
        self.run_cmake()
        print("WOO")
        build.run(self)

    def run_cmake(self):
        print("RUNNING CMAKE")
        with changed_dir("build"):
            self.spawn(['cmake','..'])
            self.spawn(['cmake','--build','.','-j','16'])


os.makedirs('build/pyodide/pyarrow/parquet',exist_ok=True)

setup(name='pyarrow',
      version='8.0',
      description='Python arrow library pyodide port',
      author='Apache',
      author_email='joe.marshall@nottingham.ac.uk',
      url='https://www.cs.nott.ac.uk/~pszjm2/',
      include_package_data=True,
      packages=['pyarrow','pyarrow.parquet'],
      package_dir = { 'pyarrow' : 'build/pyodide/pyarrow','pyarrow.parquet':'build/pyodide/pyarrow/parquet'},
      cmdclass={'build':cmake_then_build},
      package_data={'':["*.so"]}
     )
