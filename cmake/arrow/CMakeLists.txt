set(CMAKE_SHARED_LIBRARY_SUFFIX .so)

# patch an error in dataset/file_csv.cc
file(WRITE ${CMAKE_BINARY_DIR}/csv.patch [=[
*** src/arrow/dataset/file_csv.cc        2022-05-05 23:20:47.191924200 +0000
--- src/arrow/dataset/file_csv.cc 2022-05-05 23:20:55.101924200 +0000
***************
*** 20,25 ****
--- 20,26 ----
  #include <algorithm>
  #include <memory>
  #include <string>
+ #include <sstream>
  #include <unordered_set>
  #include <utility>
]=])

execute_process(COMMAND patch -p0 -i ${CMAKE_BINARY_DIR}/csv.patch 
WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} )

set(ARROW_SRCS
    array/array_base.cc
    array/array_binary.cc
    array/array_decimal.cc
    array/array_dict.cc
    array/array_nested.cc
    array/array_primitive.cc
    array/builder_adaptive.cc
    array/builder_base.cc
    array/builder_binary.cc
    array/builder_decimal.cc
    array/builder_dict.cc
    array/builder_nested.cc
    array/builder_primitive.cc
    array/builder_union.cc
    array/concatenate.cc
    array/data.cc
    array/diff.cc
    array/util.cc
    array/validate.cc
    builder.cc
    buffer.cc
    chunked_array.cc
    compare.cc
    config.cc
    datum.cc
    device.cc
    extension_type.cc
    memory_pool.cc
    pretty_print.cc
    record_batch.cc
    result.cc
    scalar.cc
    sparse_tensor.cc
    status.cc
    table.cc
    table_builder.cc
    tensor.cc
    tensor/coo_converter.cc
    tensor/csf_converter.cc
    tensor/csx_converter.cc
    type.cc
    visitor.cc
    c/bridge.cc
    io/buffered.cc
    io/caching.cc
    io/compressed.cc
    io/file.cc
    io/hdfs.cc
    io/hdfs_internal.cc
    io/interfaces.cc
    io/memory.cc
    io/slow.cc
    io/stdio.cc
    io/transform.cc
    util/async_util.cc
    util/basic_decimal.cc
    util/bit_block_counter.cc
    util/bit_run_reader.cc
    util/bit_util.cc
    util/bitmap.cc
    util/bitmap_builders.cc
    util/bitmap_ops.cc
    util/bpacking.cc
    util/byte_size.cc
    util/cancel.cc
    util/compression.cc
    util/counting_semaphore.cc
    util/cpu_info.cc
    util/decimal.cc
    util/delimiting.cc
    util/formatting.cc
    util/future.cc
    util/int_util.cc
    util/io_util.cc
    util/logging.cc
    util/key_value_metadata.cc
    util/memory.cc
    util/mutex.cc
    util/string.cc
    util/string_builder.cc
    util/task_group.cc
    util/tdigest.cc
    util/thread_pool.cc
    util/time.cc
    util/trie.cc
    util/unreachable.cc
    util/uri.cc
    util/utf8.cc
    util/value_parsing.cc
    vendored/base64.cpp
    vendored/datetime/tz.cpp
    vendored/double-conversion/bignum.cc
    vendored/double-conversion/double-conversion.cc
    vendored/double-conversion/bignum-dtoa.cc
    vendored/double-conversion/fast-dtoa.cc
    vendored/double-conversion/cached-powers.cc
    vendored/double-conversion/fixed-dtoa.cc
    vendored/double-conversion/diy-fp.cc
    vendored/double-conversion/strtod.cc)

set(ARROW_C_SRCS
    vendored/musl/strptime.c
    vendored/uriparser/UriCommon.c
    vendored/uriparser/UriCompare.c
    vendored/uriparser/UriEscape.c
    vendored/uriparser/UriFile.c
    vendored/uriparser/UriIp4Base.c
    vendored/uriparser/UriIp4.c
    vendored/uriparser/UriMemory.c
    vendored/uriparser/UriNormalizeBase.c
    vendored/uriparser/UriNormalize.c
    vendored/uriparser/UriParseBase.c
    vendored/uriparser/UriParse.c
    vendored/uriparser/UriQuery.c
    vendored/uriparser/UriRecompose.c
    vendored/uriparser/UriResolve.c
    vendored/uriparser/UriShorten.c)

# Disable DLL exports in vendored uriparser library
add_definitions(-DURI_STATIC_BUILD)

if(ARROW_DATASET)

      list(APPEND
           ARROW_SRCS
        dataset/dataset.cc
        dataset/dataset_writer.cc
        dataset/discovery.cc
        dataset/file_base.cc
        dataset/file_ipc.cc
        dataset/partition.cc
        dataset/plan.cc
        dataset/projector.cc
        dataset/scanner.cc)


    if(ARROW_CSV)
      list(APPEND 
        ARROW_SRCS dataset/file_csv.cc)
    endif()

    if(ARROW_ORC)
      list(APPEND 
        ARROW_SRCS dataset/file_orc.cc)
    endif()

if(ARROW_PARQUET)
  list(APPEND
    ARROW_SRCS dataset/file_parquet.cc)
endif()
endif()

if(ARROW_FILESYSTEM)
  if(ARROW_HDFS)
    add_definitions(-DARROW_HDFS)
  endif()

  list(APPEND
       ARROW_SRCS
       filesystem/filesystem.cc
       filesystem/localfs.cc
       filesystem/mockfs.cc
       filesystem/path_util.cc
       filesystem/util_internal.cc)

  if(ARROW_GCS)
    list(APPEND ARROW_SRCS filesystem/gcsfs.cc filesystem/gcsfs_internal.cc)
    set_source_files_properties(filesystem/gcsfs.cc filesystem/gcsfs_internal.cc
                                PROPERTIES SKIP_PRECOMPILE_HEADERS ON
                                           SKIP_UNITY_BUILD_INCLUSION ON)
  endif()
  if(ARROW_HDFS)
    list(APPEND ARROW_SRCS filesystem/hdfs.cc)
  endif()
  if(ARROW_S3)
    list(APPEND ARROW_SRCS filesystem/s3fs.cc)
    set_source_files_properties(filesystem/s3fs.cc
                                PROPERTIES SKIP_PRECOMPILE_HEADERS ON
                                           SKIP_UNITY_BUILD_INCLUSION ON)
  endif()
endif()

if(ARROW_IPC)
  list(APPEND
       ARROW_SRCS
       ipc/dictionary.cc
       ipc/feather.cc
       ipc/message.cc
       ipc/metadata_internal.cc
       ipc/options.cc
       ipc/reader.cc
       ipc/writer.cc)

  if(ARROW_JSON)
    list(APPEND ARROW_SRCS ipc/json_simple.cc)
  endif()
endif()

if(ARROW_JSON)
  list(APPEND
       ARROW_SRCS
       json/options.cc
       json/chunked_builder.cc
       json/chunker.cc
       json/converter.cc
       json/object_parser.cc
       json/object_writer.cc
       json/parser.cc
       json/reader.cc)
endif()


if(ARROW_CSV)
  list(APPEND
       ARROW_SRCS
       csv/converter.cc
       csv/chunker.cc
       csv/column_builder.cc
       csv/column_decoder.cc
       csv/options.cc
       csv/parser.cc
       csv/reader.cc)
  if(ARROW_COMPUTE)
    list(APPEND ARROW_SRCS csv/writer.cc)
  endif()
endif()

if(ARROW_COMPUTE)
  list(APPEND
       ARROW_SRCS
       compute/api_aggregate.cc
       compute/api_scalar.cc
       compute/api_vector.cc
       compute/cast.cc
       compute/exec.cc
       compute/exec/aggregate_node.cc
       compute/exec/exec_plan.cc
       compute/exec/expression.cc
       compute/exec/filter_node.cc
       compute/exec/hash_join.cc
       compute/exec/hash_join_dict.cc
       compute/exec/hash_join_node.cc
       compute/exec/ir_consumer.cc
       compute/exec/key_compare.cc
       compute/exec/key_encode.cc
       compute/exec/key_hash.cc
       compute/exec/key_map.cc
       compute/exec/order_by_impl.cc
       compute/exec/project_node.cc
       compute/exec/sink_node.cc
       compute/exec/source_node.cc
       compute/exec/task_util.cc
       compute/exec/union_node.cc
       compute/exec/util.cc
       compute/function.cc
       compute/function_internal.cc
       compute/kernel.cc
       compute/registry.cc
       compute/kernels/aggregate_basic.cc
       compute/kernels/aggregate_mode.cc
       compute/kernels/aggregate_quantile.cc
       compute/kernels/aggregate_tdigest.cc
       compute/kernels/aggregate_var_std.cc
       compute/kernels/codegen_internal.cc
       compute/kernels/hash_aggregate.cc
       compute/kernels/row_encoder.cc
       compute/kernels/scalar_arithmetic.cc
       compute/kernels/scalar_boolean.cc
       compute/kernels/scalar_cast_boolean.cc
       compute/kernels/scalar_cast_dictionary.cc
       compute/kernels/scalar_cast_internal.cc
       compute/kernels/scalar_cast_nested.cc
       compute/kernels/scalar_cast_numeric.cc
       compute/kernels/scalar_cast_string.cc
       compute/kernels/scalar_cast_temporal.cc
       compute/kernels/scalar_compare.cc
       compute/kernels/scalar_if_else.cc
       compute/kernels/scalar_nested.cc
       compute/kernels/scalar_random.cc
       compute/kernels/scalar_set_lookup.cc
       compute/kernels/scalar_string_ascii.cc
       compute/kernels/scalar_string_utf8.cc
       compute/kernels/scalar_temporal_binary.cc
       compute/kernels/scalar_temporal_unary.cc
       compute/kernels/scalar_validity.cc
       compute/kernels/util_internal.cc
       compute/kernels/vector_array_sort.cc
       compute/kernels/vector_hash.cc
       compute/kernels/vector_nested.cc
       compute/kernels/vector_replace.cc
       compute/kernels/vector_selection.cc
       compute/kernels/vector_sort.cc)
endif()

if(ARROW_WITH_BROTLI)
  add_definitions(-DARROW_WITH_BROTLI)
  list(APPEND ARROW_SRCS util/compression_brotli.cc)
endif()

if(ARROW_WITH_BZ2)
  add_definitions(-DARROW_WITH_BZ2)
  list(APPEND ARROW_SRCS util/compression_bz2.cc)
endif()

if(ARROW_WITH_LZ4)
  add_definitions(-DARROW_WITH_LZ4)
  list(APPEND ARROW_SRCS util/compression_lz4.cc)
endif()

if(ARROW_WITH_OPENTELEMETRY)
  list(APPEND ARROW_SRCS util/tracing_internal.cc)
endif()

if(ARROW_WITH_SNAPPY)
  add_definitions(-DARROW_WITH_SNAPPY)
  list(APPEND ARROW_SRCS util/compression_snappy.cc)
endif()

if(ARROW_WITH_ZLIB)
  add_definitions(-DARROW_WITH_ZLIB)
  list(APPEND ARROW_SRCS util/compression_zlib.cc)
endif()

if(ARROW_WITH_ZSTD)
  add_definitions(-DARROW_WITH_ZSTD)
  list(APPEND ARROW_SRCS util/compression_zstd.cc)
endif()

list(TRANSFORM ARROW_SRCS PREPEND ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/)
list(TRANSFORM ARROW_C_SRCS PREPEND ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/)

set(ARROW_PYTHON_SRCS
    arrow_to_pandas.cc
    benchmark.cc
    common.cc
    datetime.cc
    decimal.cc
    deserialize.cc
    extension_type.cc
    gdb.cc
    helpers.cc
    inference.cc
    init.cc
    io.cc
    ipc.cc
    numpy_convert.cc
    numpy_to_arrow.cc
    python_to_arrow.cc
    pyarrow.cc
    serialize.cc)

set_source_files_properties(init.cc PROPERTIES SKIP_PRECOMPILE_HEADERS ON
                                               SKIP_UNITY_BUILD_INCLUSION ON)

if(ARROW_CSV)
  list(APPEND ARROW_PYTHON_SRCS csv.cc)
endif()

if(ARROW_FILESYSTEM)
  list(APPEND ARROW_PYTHON_SRCS filesystem.cc)
endif()

if(PARQUET_REQUIRE_ENCRYPTION)
  list(APPEND ARROW_PYTHON_SRCS parquet_encryption.cc)
endif()

list(TRANSFORM ARROW_PYTHON_SRCS PREPEND ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/)

set(PARQUET_SRCS
    arrow/path_internal.cc
    arrow/reader.cc
    arrow/reader_internal.cc
    arrow/schema.cc
    arrow/schema_internal.cc
    arrow/writer.cc
    bloom_filter.cc
    column_reader.cc
    column_scanner.cc
    column_writer.cc
    encoding.cc
    encryption/encryption.cc
    encryption/internal_file_decryptor.cc
    encryption/internal_file_encryptor.cc
    exception.cc
    file_reader.cc
    file_writer.cc
    level_comparison.cc
    level_conversion.cc
    metadata.cc
    murmur3.cc
    platform.cc
    printer.cc
    properties.cc
    schema.cc
    statistics.cc
    stream_reader.cc
    stream_writer.cc
    types.cc)

set (GENERATED_SRCS    
parquet_constants.cpp
parquet_types.cpp
)


if(PARQUET_REQUIRE_ENCRYPTION)
  set(PARQUET_SRCS ${PARQUET_SRCS} encryption/encryption_internal.cc)
  # Encryption key management
  set(PARQUET_SRCS
      ${PARQUET_SRCS}
      encryption/crypto_factory.cc
      encryption/file_key_unwrapper.cc
      encryption/file_key_wrapper.cc
      encryption/kms_client.cc
      encryption/key_material.cc
      encryption/key_metadata.cc
      encryption/key_toolkit.cc
      encryption/key_toolkit_internal.cc
      encryption/local_wrap_kms_client.cc)
else()
  set(PARQUET_SRCS ${PARQUET_SRCS} encryption/encryption_internal_nossl.cc)
endif()

list(TRANSFORM PARQUET_SRCS PREPEND ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/)
list(TRANSFORM GENERATED_SRCS PREPEND ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/generated/)

set_property(SOURCE util/io_util.cc
           APPEND_STRING
           PROPERTY COMPILE_FLAGS " -Wno-unused-macros -stdlib=libc++")


include_directories(flatbuffers-src/include)
include_directories(src)

configure_file(src/parquet/parquet_version.h.in ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/parquet_version.h @ONLY)

# Build Arrow as a static library
set(ARROW_BUILD_STATIC ON)
if (PSP_WASM_BUILD)
    set(CMAKE_POSITION_INDEPENDENT_CODE OFF)
elseif(PSP_CPP_BUILD OR PSP_PYTHON_BUILD)
    set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

add_library(arrow STATIC ${ARROW_SRCS} ${PARQUET_SRCS} ${GENERATED_SRCS} ${ARROW_PYTHON_SRCS} ${ARROW_C_SRCS})

include_directories(${CMAKE_BINARY_DIR}/rapidjson-src/include)
include_directories(/usr/local/include/)

target_compile_definitions(arrow PUBLIC ARROW_NO_DEPRECATED_API)
target_compile_definitions(arrow PUBLIC __x86_64)
target_compile_definitions(arrow PUBLIC ARROW_STATIC)

# will need built boost filesystem and system .lib to work, even though
# perspective itself does not use those dependencies
target_link_libraries(arrow
    ${double-conversion_LIBRARIES}
    ${Boost_FILESYSTEM_LIBRARY}
    ${Boost_SYSTEM_LIBRARY}
    ${ARROW_TEST_LINK_TOOLCHAIN})


#add_custom_command(OUTPUT ${FBS_OUTPUT_FILES}
#                   COMMAND ${CMAKE_BINARY_DIR}/flatbuffers-src/flatc
#                           -c
#                           -o
#                           ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/
#                           ${FBS_SRC}
#                   COMMENT "Running flatc compiler on ${FBS_SRC}"
#                   VERBATIM)

#add_custom_target(arrow_fb_files DEPENDS ${FBS_OUTPUT_FILES})
#add_dependencies(arrow arrow_fb_files)
