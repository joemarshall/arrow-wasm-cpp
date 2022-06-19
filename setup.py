import contextlib
from glob import glob
from distutils.core import setup

from distutils.command.build import build
import os
from numpy.distutils.misc_util import get_numpy_include_dirs

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
        self.run_cmake()
        build.run(self)

    def run_cmake(self):
        numpy_include_folder=get_numpy_include_dirs()[0]
        with changed_dir("build"):
            self.spawn(['cmake','..',f'-DNUMPY_INCLUDE={numpy_include_folder}'])
            self.spawn(['cmake','--build','.','-j','16'])


# make empty packages for things created during cmake or else bad things might happen
# cmake will copy the real ones across during build
def make_empty_package(name):
    os.makedirs(f'build/pyodide/pyarrow/{name}',exist_ok=True)
    init_file=f'build/pyodide/pyarrow/{name}/__init__.py'
    if not os.path.exists(init_file):
        with open(init_file,'w') as fp:
            fp.write("\n")

#make_empty_package("parquet")
make_empty_package("vendored")



setup(name='pyarrow',
      version='8.0',
      description='Python arrow library pyodide port',
      author='Apache',
      author_email='joe.marshall@nottingham.ac.uk',
      url='https://www.cs.nott.ac.uk/~pszjm2/',
      include_package_data=True,
#      packages=['pyarrow','pyarrow.parquet','pyarrow.vendored'],
#      package_dir = { 'pyarrow' : 'build/pyodide/pyarrow','pyarrow.parquet':'build/pyodide/pyarrow/parquet','pyarrow.vendored':'build/pyodide/pyarrow/vendored'},
      packages=['pyarrow','pyarrow.vendored'],
      package_dir = { 'pyarrow' : 'build/pyodide/pyarrow','pyarrow.vendored':'build/pyodide/pyarrow/vendored'},
      cmdclass={'build':cmake_then_build},
      package_data={'':["*.so"]}
     )
