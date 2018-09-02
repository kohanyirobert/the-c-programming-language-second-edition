cmake_minimum_required(VERSION 3.12.1 FATAL_ERROR)

project(the-c-programming-language-second-edition
        LANGUAGES C)

set(CMAKE_C_STANDARD 90)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

if ("${CMAKE_C_COMPILER_ID}" STREQUAL "MSVC")
        # The default compiler flags for cl are somewhat suppressed by
        # this. /Za is set to disable Microsoft extensions explicitly
        # as CMAKE_C_EXTENSIONS doesn't seem to have effect on this.
        # Otherwise flags such as /W3 will be set and that'll raise
        # too many warnings (ones which gcc doesn't pickup with C90
        # compatibility enabled).
        set(CMAKE_C_FLAGS "/Za")
endif()

enable_testing()

find_package(Python3)

function(add_python3_test target)
        add_test(NAME ${target}_test
                 COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/${target}_test.py $<TARGET_FILE:${target}>
                 WORKING_DIRECTORY ${EXECUTABLE_OUTPUT_PATH})
endfunction()

add_subdirectory(chapter-1)
