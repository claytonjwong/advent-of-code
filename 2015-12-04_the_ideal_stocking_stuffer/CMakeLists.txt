cmake_minimum_required(VERSION 3.14)
project(2015_12_04_the_ideal_stocking_stuffer)

set(CMAKE_CXX_STANDARD 17)

add_library(md5 STATIC md5.cpp)
add_executable(2015_12_04_the_ideal_stocking_stuffer main.cpp)
target_link_libraries(2015_12_04_the_ideal_stocking_stuffer md5)