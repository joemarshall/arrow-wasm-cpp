import contextlib
from glob import glob
from setuptools import setup,Extension

import setuptools
from numpy import get_include
from setuptools.command.build import build
from setuptools.command.build_ext import build_ext 
import os

@contextlib.contextmanager
def changed_dir(dirname):
    oldcwd = os.getcwd()
    if not os.path.exists(dirname):
        os.makedirs(dirname,exist_ok=True)
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
            numpy_include_folder=get_include()
            self.spawn(['cmake','..',f'-DNUMPY_INCLUDE={numpy_include_folder}','-DCMAKE_MAKE_PROGRAM=make'])
            self.spawn(['cmake','--build','.','-j','16'])


# this is just so that it builds as an extension specific to pyodide/emscripten
class do_nothing_ext(build_ext):
    def run(self):
        pass


# make empty packages for things created during cmake or else bad things might happen
# cmake will copy the real ones across during build
def make_empty_package(name):
    os.makedirs(f'build/pyodide/pyarrow/{name}',exist_ok=True)
    init_file=f'build/pyodide/pyarrow/{name}/__init__.py'
    if not os.path.exists(init_file):
        with open(init_file,'w') as fp:
            fp.write("\n")

make_empty_package("vendored")

setup(name='pyarrow',
      version='7.0',
      description='Python arrow library pyodide port',
      author='Apache',
      author_email='joe.marshall@nottingham.ac.uk',
      url='https://www.cs.nott.ac.uk/~pszjm2/',
      include_package_data=True,
      ext_modules = [Extension("ignored", [])],
      packages=['pyarrow','pyarrow.vendored'],
      package_dir = { 'pyarrow' : 'build/pyodide/pyarrow','pyarrow.vendored':'build/pyodide/pyarrow/vendored'},
      cmdclass={'build_ext':do_nothing_ext,'build':cmake_then_build},
      package_data={'':["*.so"]}
     )
