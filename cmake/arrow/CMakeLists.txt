set(CMAKE_SHARED_LIBRARY_SUFFIX .so)

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
    chunk_resolver.cc
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
#    io/hdfs.cc
#    io/hdfs_internal.cc
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
    util/debug.cc
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
    util/tracing.cc
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

list(TRANSFORM ARROW_SRCS PREPEND ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/)

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
    ../generated/parquet_constants.cpp
    ../generated/parquet_types.cpp
    platform.cc
    printer.cc
    properties.cc
    schema.cc
    statistics.cc
    stream_reader.cc
    stream_writer.cc
    types.cc)

list(TRANSFORM PARQUET_SRCS PREPEND ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/)


set_property(SOURCE util/io_util.cc
           APPEND_STRING
           PROPERTY COMPILE_FLAGS " -Wno-unused-macros -stdlib=libc++")

# don't do this because we don't use IPC

# make clean will delete the generated file
#set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Message_generated.h PROPERTIES GENERATED TRUE)
#set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/File_generated.h PROPERTIES GENERATED TRUE)
#set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Schema_generated.h PROPERTIES GENERATED TRUE)
#set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Tensor_generated.h PROPERTIES GENERATED TRUE)
#set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/SparseTensor_generated.h PROPERTIES GENERATED TRUE)
#set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/feather_generated.h PROPERTIES GENERATED TRUE)

#set(FBS_OUTPUT_FILES
#    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Message_generated.h
#    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/File_generated.h
#    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Schema_generated.h
#    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Tensor_generated.h
#    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/SparseTensor_generated.h
#    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/feather_generated.h)

#set(FBS_SRC
#    ${CMAKE_BINARY_DIR}/arrow-src/format/Message.fbs
#    ${CMAKE_BINARY_DIR}/arrow-src/format/File.fbs
#    ${CMAKE_BINARY_DIR}/arrow-src/format/Schema.fbs
#    ${CMAKE_BINARY_DIR}/arrow-src/format/Tensor.fbs
#    ${CMAKE_BINARY_DIR}/arrow-src/format/SparseTensor.fbs
#    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/feather.fbs)

include_directories(src)
include_directories(flatbuffers-src/include)

configure_file(src/parquet/parquet_version.h.in ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/parquet_version.h @ONLY)

# Build Arrow as a static library
set(ARROW_BUILD_STATIC ON)
if (PSP_WASM_BUILD)
    set(CMAKE_POSITION_INDEPENDENT_CODE OFF)
elseif(PSP_CPP_BUILD OR PSP_PYTHON_BUILD)
    set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

add_library(arrow STATIC ${ARROW_SRCS} ${PARQUET_SRCS})

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
