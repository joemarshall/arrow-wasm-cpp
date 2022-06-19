cmake_minimum_required(VERSION 3.7.2)


include(ExternalProject)

set(NUMPY_INCLUDE "" CACHE STRING "Path to /numpy/core/include folder from numpy")
if(NOT NUMPY_INCLUDE )
    message(FATAL_ERROR "CMake needs NUMPY_INCLUDE variable to work. setup.py sets this")
endif()
if(NOT EXISTS ${NUMPY_INCLUDE})
    message(FATAL_ERROR "Can't find NUMPY_INCLUDE folder ${NUMPY_INCLUDE}")
endif()

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/modules" ${CMAKE_MODULE_PATH})

execute_process(COMMAND which emcc OUTPUT_VARIABLE EMCC)
execute_process(COMMAND which em++ OUTPUT_VARIABLE EMPP)
string(STRIP ${EMCC} EMCC)
string(STRIP ${EMPP} EMPP)

set(CMAKE_C_COMPILER ${EMCC})
set(CMAKE_CXX_COMPILER ${EMPP})
set(CMAKE_TOOLCHAIN_FILE "$ENV{EMSDK}/upstream/emscripten/cmake/Modules/Platform/Emscripten.cmake")

set(CMAKE_AR emar)
set(CMAKE_RANLIB emranlib)
set(CMAKE_EXECUTABLE_SUFFIX ".js")

set(CMAKE_CXX_FLAGS " \
    -fPIC \
    --bind \
    --source-map-base ./build/ \
    --memory-init-file 0 \
    -Wall \
    -s WASM=1 \
    -s SIDE_MODULE=1 \
    -fcolor-diagnostics \
    -s NO_FILESYSTEM=1 \
    -s ALLOW_MEMORY_GROWTH=1 \
    -s MODULARIZE=1 \
    -s USE_BOOST_HEADERS=1 \
    -s USE_BZIP2=1 \
    -s USE_ZLIB=1  \
    ")

set(CMAKE_C_FLAGS ${CMAKE_CXX_FLAGS})

set(CMAKE_EXE_LINKER_FLAGS "")
set(CMAKE_C_LINK_FLAGS "")
set(CMAKE_CXX_LINK_FLAGS "")
set(HAVE_FLAG_SEARCH_PATHS_FIRST 0)

cmake_policy(SET CMP0077 NEW)

set(ARROW_VERSION "7.0.0")

string(REGEX MATCH "^[0-9]+\\.[0-9]+\\.[0-9]+" ARROW_BASE_VERSION "${ARROW_VERSION}")
project(arrow_wasm VERSION "${ARROW_BASE_VERSION}")


set(ARROW_VERSION_MAJOR "${arrow_wasm_VERSION_MAJOR}")
set(ARROW_VERSION_MINOR "${arrow_wasm_VERSION_MINOR}")
set(ARROW_VERSION_PATCH "${arrow_wasm_VERSION_PATCH}")
if(ARROW_VERSION_MAJOR STREQUAL ""
   OR ARROW_VERSION_MINOR STREQUAL ""
   OR ARROW_VERSION_PATCH STREQUAL "")
  message(FATAL_ERROR "Failed to determine Arrow version from '${ARROW_VERSION}'")
endif()



set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)


# set arrow flags
set(ARROW_DEPENDENCY_SOURCE BUNDLED)

set(ARROW_BUILD_BENCHMARKS OFF)
set(ARROW_BUILD_EXAMPLES OFF)
set(ARROW_BUILD_INTEGRATION OFF)
set(ARROW_BUILD_TESTS OFF)
set(ARROW_CUDA OFF)

set(ARROW_DATASET ON)
set(ARROW_FILESYSTEM ON)
set(ARROW_HDFS ON)
set(ARROW_JSON ON)
set(ARROW_COMPUTE ON)
set(ARROW_FUZZING OFF)
set(ARROW_GANDIVA OFF)
set(ARROW_OPTIONAL_INSTALL OFF)
set(ARROW_PARQUET ON)
set(ARROW_CSV ON)
#set(ARROW_WITH_BROTLI ON)
#set(ARROW_WITH_ZSTD ON)
#set(ARROW_WITH_LZ4 ON)
set(ARROW_WITH_SNAPPY ON)
set(ARROW_WITH_BZ2 ON)
set(ARROW_PYTHON ON)
set(ARROW_JNI OFF)
set(ARROW_ORC OFF)
set(ARROW_ORC OFF)
set(ARROW_IPC ON)

set(ARROW_BUILD_STATIC ON)
set(ARROW_NO_DEPRECATED_API ON)

set(RAPIDJSON_BUILD_DOC OFF)
set(RAPIDJSON_BUILD_EXAMPLES OFF)
set(RAPIDJSON_BUILD_TESTS OFF)
set(RAPIDJSON_BUILD_THIRDPARTY_GTEST OFF)
set(RAPIDJSON_BUILD_CXX11 ON)
option(RAPIDJSON_ENABLE_INSTRUMENTATION_OPT OFF)

include_directories($ENV{PYTHONINCLUDE})
include_directories(${CMAKE_BINARY_DIR}/flatbuffers-build/include/)
include_directories (/src/cpython/installs/python-3.10.2/include/python3.10/)
include_directories(${NUMPY_INCLUDE})
include_directories(${CMAKE_BINARY_DIR}/arrow-src/cpp/thirdparty/hadoop/include)


function (build_dep name)



    configure_file("${CMAKE_SOURCE_DIR}/cmake/${name}.txt.in"
                ${name}-download/CMakeLists.txt COPYONLY)

    execute_process(COMMAND ${CMAKE_COMMAND} -G "${CMAKE_GENERATOR}" -DCMAKE_BINARY_DIR="${CMAKE_BINARY_DIR}" .
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/${name}-download )

    execute_process(COMMAND ${CMAKE_COMMAND} --build .
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/${name}-download )

	if(${name} STREQUAL arrow)
        configure_file(${CMAKE_SOURCE_DIR}/cmake/arrow/CMakeLists.txt ${CMAKE_BINARY_DIR}/arrow-src/cpp/ COPYONLY)
        configure_file(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/config.h.cmake ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/config.h)
        include_directories(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/)
        include_directories(${CMAKE_BINARY_DIR}/arrow-src/cpp/thirdparty/flatbuffers/include)
        add_subdirectory(${CMAKE_BINARY_DIR}/${name}-src/cpp
            ${CMAKE_BINARY_DIR}/${name}-build
            EXCLUDE_FROM_ALL)
	elseif(${name} STREQUAL flatbuffers)
        # add to include folders
        include_directories(${CMAKE_BINARY_DIR}/${name}-src/include)
    elseif(${name} STREQUAL thrift)
        include_directories(${CMAKE_BINARY_DIR}/thrift-src/lib/cpp/src)
        include_directories(${CMAKE_BINARY_DIR}/thrift-build)
    	link_directories(${CMAKE_BINARY_DIR}/thrift-build/lib)
    elseif(${name} STREQUAL snappy)
        configure_file(${CMAKE_SOURCE_DIR}/cmake/snappy/CMakeLists.txt ${CMAKE_BINARY_DIR}/snappy-src/ COPYONLY)
        include_directories(${CMAKE_BINARY_DIR}/${name}-src/include)
        include_directories(${CMAKE_BINARY_DIR}/${name}-src)
        include_directories(${CMAKE_BINARY_DIR}/${name}-build)
    	link_directories(${CMAKE_BINARY_DIR}/snappy-build)
        add_subdirectory(${CMAKE_BINARY_DIR}/${name}-src
            ${CMAKE_BINARY_DIR}/${name}-build
            EXCLUDE_FROM_ALL)
    else()
        include_directories(${CMAKE_BINARY_DIR}/${name}-src/include)
        include_directories(${CMAKE_BINARY_DIR}/${name}-src)
        add_subdirectory(${CMAKE_BINARY_DIR}/${name}-src
            ${CMAKE_BINARY_DIR}/${name}-build
            EXCLUDE_FROM_ALL)
    endif()
endfunction()

function (build_cython_submodule name)
add_custom_command(OUTPUT ${CMAKE_BINARY_DIR}/arrow-src/python/pyarrow/${name}.cpp
	COMMAND python -m cython --cplus  ${CMAKE_BINARY_DIR}/arrow-src/python/pyarrow/${name}.pyx)
add_executable(${name} ${CMAKE_BINARY_DIR}/arrow-src/python/pyarrow/${name}.cpp)
set_target_properties(${name} PROPERTIES OUTPUT_NAME ${name})
set_target_properties(${name} PROPERTIES RUNTIME_OUTPUT_DIRECTORY "./pyodide/pyarrow")
set_target_properties(${name} PROPERTIES SUFFIX .so)
add_dependencies(${name} arrow_pyodide)
endfunction()



function(copy_python_source name)
# copy after arrow is downloaded and everything is build, not in configure step
    # make sure folder exists
    get_filename_component(OWNER_DIR ${CMAKE_BINARY_DIR}/pyodide/pyarrow/${name} DIRECTORY)
    file(MAKE_DIRECTORY ${OWNER_DIR})
    add_custom_command(
        TARGET arrow_pyodide PRE_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_BINARY_DIR}/arrow-src/python/pyarrow/${name}
                ${CMAKE_BINARY_DIR}/pyodide/pyarrow/${name}
        )
endfunction()

build_dep(snappy)
build_dep(thrift)
#build_dep(flatbuffers)
build_dep(rapidjson)
build_dep(arrow)

# make the shared library for arrow
file(WRITE ${CMAKE_BINARY_DIR}/null.cpp "")
add_executable(arrow_pyodide ${CMAKE_BINARY_DIR}/null.cpp)
set_target_properties(arrow_pyodide PROPERTIES RUNTIME_OUTPUT_DIRECTORY "./pyodide/pyarrow/")
set_target_properties(arrow_pyodide PROPERTIES OUTPUT_NAME "libarrow")
set_target_properties(arrow_pyodide PROPERTIES SUFFIX ".so")
target_link_libraries(arrow_pyodide arrow thrift snappy)

# make the python module
# first modify code to disable threading
add_custom_command(
    TARGET arrow_pyodide PRE_BUILD
            COMMAND find ${CMAKE_BINARY_DIR}/arrow-src/python/pyarrow/ -type f -exec sed -i 's/use_threads=True/use_threads=False/g' {} "\;"
            COMMAND find ${CMAKE_BINARY_DIR}/arrow-src/python/pyarrow/ -type f -exec sed -i 's/pre_buffer=True/pre_buffer=False/g' {} "\;"
    )





build_cython_submodule(lib)
#build_cython_submodule(_plasma)
build_cython_submodule(_dataset)
build_cython_submodule(_hdfs)
build_cython_submodule(_hdfsio)
build_cython_submodule(_fs)
# remove dataset API because it is threaded
#build_cython_submodule(_dataset_parquet)
#build_cython_submodule(_feather)
build_cython_submodule(_csv)
build_cython_submodule(_json)
build_cython_submodule(_parquet)
#build_cython_submodule(gandiva)
#build_cython_submodule(_s3fs)
#build_cython_submodule(_exec_plan)
#build_cython_submodule(_cuda)
#build_cython_submodule(_orc)
#build_cython_submodule(_dataset_orc)
build_cython_submodule(_compute)
#build_cython_submodule(_flight)

copy_python_source(_compute_docstrings.py)
copy_python_source(benchmark.py)
copy_python_source(cffi.py)
copy_python_source(compat.py)
copy_python_source(compute.py)
copy_python_source(csv.py)
copy_python_source(cuda.py)
# remove dataset API because it is heavily threaded
#copy_python_source(dataset.py)
copy_python_source(feather.py)
copy_python_source(filesystem.py)
copy_python_source(flight.py)
copy_python_source(fs.py)
copy_python_source(hdfs.py)
copy_python_source(ipc.py)
copy_python_source(json.py)
copy_python_source(jvm.py)
copy_python_source(orc.py)
copy_python_source(pandas_compat.py)
copy_python_source(parquet.py)
copy_python_source(plasma.py)
copy_python_source(serialization.py)
#copy_python_source(tests/test_dataset.py)
#copy_python_source(tests/test_types.py)
#copy_python_source(tests/test_filesystem.py)
#copy_python_source(tests/test_cuda.py)
#copy_python_source(tests/test_orc.py)
#copy_python_source(tests/deserialize_buffer.py)
#copy_python_source(tests/test_pandas.py)
#copy_python_source(tests/test_gandiva.py)
#copy_python_source(tests/test_serialization.py)
#copy_python_source(tests/test_feather.py)
#copy_python_source(tests/test_plasma.py)
#copy_python_source(tests/test_cuda_numba_interop.py)
#copy_python_source(tests/test_cython.py)
#copy_python_source(tests/test_hdfs.py)
#copy_python_source(tests/test_array.py)
#copy_python_source(tests/test_io.py)
#copy_python_source(tests/test_scalars.py)
#copy_python_source(tests/test_extension_type.py)
#copy_python_source(tests/test_memory.py)
#copy_python_source(tests/test_deprecations.py)
#copy_python_source(tests/test_plasma_tf_op.py)
#copy_python_source(tests/test_compute.py)
#copy_python_source(tests/test_strategies.py)
#copy_python_source(tests/test_jvm.py)
#copy_python_source(tests/test_sparse_tensor.py)
#copy_python_source(tests/conftest.py)
#copy_python_source(tests/test_schema.py)
#copy_python_source(tests/test_convert_builtin.py)
#copy_python_source(tests/test_gdb.py)
#copy_python_source(tests/test_serialization_deprecated.py)
#copy_python_source(tests/test_ipc.py)
#copy_python_source(tests/test_fs.py)
#copy_python_source(tests/pandas_examples.py)
#copy_python_source(tests/util.py)
#copy_python_source(tests/test_csv.py)
#copy_python_source(tests/strategies.py)
#copy_python_source(tests/test_misc.py
#copy_python_source(tests/test_table.py
#copy_python_source(tests/test_cffi.py
#copy_python_source(tests/parquet/test_dataset.py
#copy_python_source(tests/parquet/test_metadata.py
#copy_python_source(tests/parquet/test_pandas.py
#copy_python_source(tests/parquet/test_data_types.py
#copy_python_source(tests/parquet/test_compliant_nested_type.py
#copy_python_source(tests/parquet/common.py
#copy_python_source(tests/parquet/conftest.py
#copy_python_source(tests/parquet/test_basic.py
#copy_python_source(tests/parquet/test_parquet_file.py
#copy_python_source(tests/parquet/test_datetime.py
#copy_python_source(tests/parquet/test_parquet_writer.py
#copy_python_source(tests/test_adhoc_memory_leak.py
#copy_python_source(tests/pandas_threaded_import.py
#copy_python_source(tests/test_json.py
#copy_python_source(tests/__init__.py
#copy_python_source(tests/test_util.py
#copy_python_source(tests/arrow_7980.py
#copy_python_source(tests/test_builder.py
#copy_python_source(tests/test_flight.py
#copy_python_source(tests/test_tensor.py
copy_python_source(types.py)
copy_python_source(util.py)
copy_python_source(vendored/docscrape.py)
copy_python_source(vendored/version.py)
copy_python_source(vendored/__init__.py)

#copy_python_source(__init__.py)
file(READ ${CMAKE_BINARY_DIR}/arrow-src/python/pyarrow/__init__.py OLD_INIT_PY)
file(WRITE ${CMAKE_BINARY_DIR}/pyodide/pyarrow/__init__.py [=[
# load libarrow into the global namespace on first import otherwise all things depending on it won't work right
import pyodide as __pyodide
import pyodide_js as __pjs
import js as __js
__pjs._module.loadDynamicLibrary("/lib/python3.10/site-packages/pyarrow/libarrow.so",__pyodide.to_js({"global":True,"loadAsync":False},dict_converter=__js.Object.fromEntries))

]=]
)
file(APPEND ${CMAKE_BINARY_DIR}/pyodide/pyarrow/__init__.py ${OLD_INIT_PY})
file(APPEND ${CMAKE_BINARY_DIR}/pyodide/pyarrow/__init__.py __version__="8.0.0")
copy_python_source(compat.py)
copy_python_source(ipc.py)

file(WRITE ${CMAKE_BINARY_DIR}/pyodide/setup.cfg [=[
[metadata]
name = pyarrow
version = 8.0

[options]
include_package_data = True
package_dir= .
packages=pyarrow
python_requires '>=3.7'

[options.package_data]
* = *.so
]=])
