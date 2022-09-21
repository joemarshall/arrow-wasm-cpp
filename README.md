Standalone Apache Arrow compiled to WebAssembly for pyodide, extracted from https://github.com/finos/perspective

Currently builds Apache Arrow version `7.0.0`.

The build is a setup.py wrapper around cmake.

# Build instructions

You can build a wheel for pyodide with standalone pyodide-build. To do this, you need to:
1) Install the correct python version for the pyodide build you are targeting. e.g. For pyodide 0.21, this is 3.10.2
2) Install emscripten sdk
3) Install the emscripten version for your pyodide (e.g. for pyodide 0.21 this is 3.1.14)
4) Install `pyodide-build` module with pip install pyodide-build
5) Run `pyodide build`
e.g. with conda, I did:
```
# create venv with python 3.10.2
conda create -n py3102 python=3.10.2
conda activate py3102

# get EMSDK manager
git clone https://github.com/emscripten-core/emsdk.git
# go into the EMSDK folder
cd emsdk
./emsdk install 3.1.14
./emsdk activate 3.1.14
# make sure emcc etc. are on the path
source emsdk_env.sh

# install pyodide-build in this venv
pip install pyodide-build

# build a pyodide package
pyodide build
# at this point you should have a wheel file in the dist subfolder.

```

# Limitations

There are several limitations of this library compared to normal pyarrow:
1) Datasets is not included - this is because there is no threading support yet in pyodide. Once threads turn up this should work fine.
2) There's no socket support in pyodide, so things relying on network connection don't work.
3) Some other things which rely on threading (e.g. readahead) won't work and will fail with weird errors.
