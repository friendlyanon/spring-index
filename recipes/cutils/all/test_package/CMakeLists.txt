cmake_minimum_required(VERSION 3.21)

project(test_package CXX)

find_package(CUtils REQUIRED)

add_executable(test_package test_package.cpp)
target_link_libraries(test_package PRIVATE CUtils::CUtils)
