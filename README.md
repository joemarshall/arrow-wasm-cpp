Standalone Apache Arrow compiled to WebAssembly for pyodide, extracted from https://github.com/finos/perspective

Currently builds Apache Arrow version `7.0.0`.

Build inside a pyodide build folder, using the included meta file.

The build is a setup.py wrapper around cmake.

# Limitations

There are several limitations of this library compared to normal pyarrow:
1) Datasets is not included - this is because there is no threading support yet in pyodide. Once threads turn up this should work fine.
2) There's no socket support in pyodide, so things relying on network connection don't work.
3) Some other things which rely on threading (e.g. readahead) won't work and will fail with weird errors.
