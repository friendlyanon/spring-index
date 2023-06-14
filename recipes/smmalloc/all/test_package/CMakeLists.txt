cmake_minimum_required(VERSION 3.21)

project(test_package CXX)

find_package(smmalloc REQUIRED)

add_executable(test_package test_package.cpp)
target_link_libraries(test_package PRIVATE smmalloc::smmalloc)
