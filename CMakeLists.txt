cmake_minimum_required (VERSION 3.21)
project (SHARP)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

find_package(Python3 REQUIRED COMPONENTS Interpreter)
find_package(Mono 6.12 REQUIRED COMPONENTS)

find_program(ILASM_EXECUTABLE ilasm)  
if(NOT ILASM_EXECUTABLE)
    message(FATAL_ERROR "ilasm not found.")
endif()

find_program(LLVM_CONFIG NAMES llvm-config REQUIRED HINTS /usr/bin/llvm-config)
message(STATUS "Using llvm-config: ${LLVM_CONFIG}")
exec_program("${LLVM_CONFIG} --bindir" OUTPUT_VARIABLE LLVM_BINDIR)

set(SHARP_BIN_DIR ${CMAKE_CURRENT_SOURCE_DIR}/sharp-cli/bin/Debug/net6.0)
set(SHARP_SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR})

configure_file("${CMAKE_CURRENT_SOURCE_DIR}/integration-test/lit.site.cfg.py.in" "${CMAKE_CURRENT_BINARY_DIR}/integration-test/lit.site.cfg.py" @ONLY)
