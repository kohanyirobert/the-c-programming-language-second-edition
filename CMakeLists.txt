cmake_minimum_required(VERSION 3.12.1 FATAL_ERROR)

project(the-c-programming-language-second-edition
        VERSION 0.0.0.1
        LANGUAGES C)

set(CMAKE_C_STANDARD 90)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

enable_testing()

find_package(Python3)

function(add_python3_test target)
        add_test(NAME ${target}_test
                 COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/${target}_test.py $<TARGET_FILE:${target}>
                 WORKING_DIRECTORY ${EXECUTABLE_OUTPUT_PATH})
endfunction()

add_subdirectory(chapter-1)
