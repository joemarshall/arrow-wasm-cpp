set(CMAKE_SHARED_LIBRARY_SUFFIX .so)

set(ARROW_SRCS
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/pretty_print.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/partition.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/projector.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/dataset.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/file_orc.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/dataset_writer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/discovery.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/scanner.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/file_csv.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/file_parquet.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/file_base.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/plan.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dataset/file_ipc.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/result.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/scalar.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/device.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/builder_base.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/builder_union.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/validate.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/util.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/array_primitive.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/array_base.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/array_nested.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/diff.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/builder_binary.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/array_binary.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/builder_primitive.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/builder_nested.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/concatenate.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/array_decimal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/builder_dict.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/array_dict.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/data.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/builder_decimal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/array/builder_adaptive.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/tensor/csx_converter.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/tensor/coo_converter.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/tensor/csf_converter.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/config.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/filesystem/mockfs.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/filesystem/filesystem.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/filesystem/localfs.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/filesystem/util_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/filesystem/path_util.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/chunk_resolver.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/stream_fuzz.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/reader.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/options.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/file_to_stream.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/dictionary.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/tensor_stream_fuzz.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/metadata_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/file_fuzz.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/writer.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/feather.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/generate_fuzz_corpus.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/stream_to_file.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/generate_tensor_fuzz_corpus.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/message.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/json_simple.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/type.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/json/reader.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/json/options.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/json/chunked_builder.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/json/converter.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/json/object_parser.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/json/object_writer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/json/parser.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/json/chunker.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/chunked_array.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/vendored/double-conversion/strtod.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/vendored/double-conversion/bignum-dtoa.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/vendored/double-conversion/fast-dtoa.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/vendored/double-conversion/cached-powers.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/vendored/double-conversion/bignum.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/vendored/double-conversion/diy-fp.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/vendored/double-conversion/double-conversion.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/vendored/double-conversion/fixed-dtoa.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bit_util.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/cancel.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/mutex.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bitmap_builders.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bit_run_reader.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/compression.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/async_util.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/logging.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/key_value_metadata.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/compression_bz2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/formatting.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bpacking_avx2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/uri.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/string_builder.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bpacking_neon.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bit_block_counter.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bitmap_ops.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/tdigest.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/counting_semaphore.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/string.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/compression_lz4.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/debug.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bitmap.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/int_util.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/value_parsing.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/compression_snappy.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/basic_decimal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/trie.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bpacking_avx512.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/compression_zlib.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/byte_size.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/compression_zstd.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/time.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/unreachable.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/delimiting.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/tracing_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/memory.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/future.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/io_util.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/thread_pool.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/bpacking.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/tracing.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/cpu_info.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/decimal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/utf8.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/task_group.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/util/compression_brotli.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/datum.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/server.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/server_auth.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport.cc
## ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport_server.cc
 #${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/grpc/grpc_server.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/grpc/protocol_grpc_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/grpc/grpc_client.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/grpc/util_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/grpc/serialization_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/ucx/ucx_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/ucx/ucx_client.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/ucx/util_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/ucx/ucx_server.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/transport/ucx/ucx.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/types.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/example/sqlite_sql_info.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/example/sqlite_statement.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/example/sqlite_type_info.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/example/sqlite_tables_schema_batch_reader.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/example/sqlite_server.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/example/sqlite_statement_batch_reader.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/server.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/sql_info_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/client.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/sql/column_metadata.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/cookie_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/perf_server.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/try_compile/check_tls_opts_134.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/try_compile/check_tls_opts_136.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/try_compile/check_tls_opts_132.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/try_compile/check_tls_opts_127.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/try_compile/check_tls_opts_143.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/client.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/client_cookie_middleware.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/flight/serialization_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/status.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compare.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/csv/reader.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/csv/options.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/csv/column_decoder.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/csv/column_builder.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/csv/converter.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/csv/writer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/csv/parser.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/csv/chunker.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dbi/hiveserver2/sample_usage.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dbi/hiveserver2/operation.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dbi/hiveserver2/util.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dbi/hiveserver2/session.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dbi/hiveserver2/types.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dbi/hiveserver2/service.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dbi/hiveserver2/columnar_row_set.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/dbi/hiveserver2/thrift_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/engine/substrait/plan_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/engine/substrait/serde.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/engine/substrait/relation_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/engine/substrait/extension_types.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/engine/substrait/type_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/engine/substrait/expression_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/engine/substrait/extension_set.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/function.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernel.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/key_hash.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/options.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/exec_plan.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/aggregate_node.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/util.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/bloom_filter_avx2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/partition_util.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/hash_join_dict.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/key_encode.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/bloom_filter.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/hash_join.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/tpch_node.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/task_util.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/hash_join_node.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/sink_node.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/union_node.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/key_map_avx2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/expression.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/key_compare.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/order_by_impl.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/filter_node.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/key_compare_avx2.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/util_avx2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/source_node.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/key_hash_avx2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/ir_consumer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/key_map.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/project_node.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec/key_encode_avx2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_if_else.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_cast_dictionary.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_string_ascii.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/vector_hash.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_cast_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/vector_selection.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/aggregate_quantile.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_compare.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_temporal_unary.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_set_lookup.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_random.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/hash_aggregate.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_cast_boolean.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/vector_nested.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_validity.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/aggregate_basic_avx512.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/row_encoder.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_arithmetic.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/aggregate_mode.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/vector_replace.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/aggregate_basic.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/vector_array_sort.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_cast_string.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/vector_sort.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_nested.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/util_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_boolean.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_cast_nested.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_cast_numeric.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/aggregate_var_std.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_temporal_binary.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/aggregate_tdigest.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/codegen_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_string_utf8.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/aggregate_basic_avx2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/kernels/scalar_cast_temporal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/registry.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/api_vector.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/api_aggregate.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/cast.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/function_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/light_array.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/exec.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/compute/api_scalar.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/memory_pool.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/arrow_to_pandas.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/gdb.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/helpers.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/benchmark.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/datetime.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/numpy_to_arrow.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/numpy_convert.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/io.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/serialize.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/ipc.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/init.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/filesystem.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/inference.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/pyarrow.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/parquet_encryption.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/common.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/extension_type.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/python_to_arrow.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/deserialize.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/csv.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/decimal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/python/flight.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/extension_type.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/table.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/table_builder.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/stdio.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/caching.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/file.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/buffered.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/hdfs_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/memory.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/transform.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/compressed.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/slow.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/interfaces.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/io/hdfs.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/tensor.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/sparse_tensor.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/builder.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/record_batch.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/c/bridge.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/buffer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/visitor.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encoding.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/metadata.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/level_conversion.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/printer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/column_reader.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/key_toolkit.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/test_encryption_util.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/key_metadata.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/internal_file_decryptor.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/encryption.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/key_material.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/file_key_wrapper.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/crypto_factory.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/kms_client.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/key_toolkit_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/encryption_internal.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/file_key_unwrapper.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/test_in_memory_kms.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/local_wrap_kms_client.cc
# ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/internal_file_encryptor.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/encryption/encryption_internal_nossl.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/arrow/reader.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/arrow/fuzz.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/arrow/reader_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/arrow/writer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/arrow/generate_fuzz_corpus.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/arrow/path_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/arrow/schema_internal.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/arrow/schema.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/stream_reader.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/file_reader.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/level_comparison_avx2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/types.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/bloom_filter.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/level_comparison.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/exception.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/properties.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/column_scanner.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/platform.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/stream_writer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/level_conversion_bmi2.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/column_writer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/statistics.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/file_writer.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/murmur3.cc
 ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/schema.cc
)


set_property(SOURCE util/io_util.cc
           APPEND_STRING
           PROPERTY COMPILE_FLAGS " -Wno-unused-macros -stdlib=libc++")

# make clean will delete the generated file
set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Message_generated.h PROPERTIES GENERATED TRUE)
set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/File_generated.h PROPERTIES GENERATED TRUE)
set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Schema_generated.h PROPERTIES GENERATED TRUE)
set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Tensor_generated.h PROPERTIES GENERATED TRUE)
set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/SparseTensor_generated.h PROPERTIES GENERATED TRUE)
set_source_files_properties(${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/feather_generated.h PROPERTIES GENERATED TRUE)

set(FBS_OUTPUT_FILES
    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Message_generated.h
    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/File_generated.h
    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Schema_generated.h
    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/Tensor_generated.h
    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/SparseTensor_generated.h
    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/feather_generated.h)

set(FBS_SRC
    ${CMAKE_BINARY_DIR}/arrow-src/format/Message.fbs
    ${CMAKE_BINARY_DIR}/arrow-src/format/File.fbs
    ${CMAKE_BINARY_DIR}/arrow-src/format/Schema.fbs
    ${CMAKE_BINARY_DIR}/arrow-src/format/Tensor.fbs
    ${CMAKE_BINARY_DIR}/arrow-src/format/SparseTensor.fbs
    ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/feather.fbs)

include_directories(src)
include_directories(../../flatbuffers/include)

configure_file(src/parquet/parquet_version.h.in ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/parquet/parquet_version.h @ONLY)

# Build Arrow as a static library
set(ARROW_BUILD_STATIC ON)
if (PSP_WASM_BUILD)
    set(CMAKE_POSITION_INDEPENDENT_CODE OFF)
elseif(PSP_CPP_BUILD OR PSP_PYTHON_BUILD)
    set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

add_library(arrow STATIC ${ARROW_SRCS})

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

find_package(Flatbuffers)

add_custom_command(OUTPUT ${FBS_OUTPUT_FILES}
                   COMMAND ${FLATBUFFERS_COMPILER}
                           -c
                           -o
                           ${CMAKE_BINARY_DIR}/arrow-src/cpp/src/arrow/ipc/
                           ${FBS_SRC}
                   DEPENDS ${FLATBUFFERS_COMPILER}
                   COMMENT "Running flatc compiler on ${FBS_SRC}"
                   VERBATIM)

add_custom_target(arrow_fb_files DEPENDS ${FBS_OUTPUT_FILES})
add_dependencies(arrow arrow_fb_files)
