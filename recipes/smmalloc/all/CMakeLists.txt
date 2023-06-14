cmake_minimum_required(VERSION 3.15)

project(smmalloc CXX)

set(root "source_subfolder/SmMalloc")

add_library(smmalloc STATIC
"${root}/smmalloc.cpp"
"${root}/smmalloc_generic.cpp"
"${root}/smmalloc_tls.cpp"
)

include(GNUInstallDirs)

install(TARGETS smmalloc EXPORT smmallocConfig INCLUDES DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")
install(FILES "${root}/smmalloc.h" DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/smmalloc")
install(EXPORT smmallocConfig NAMESPACE smmalloc:: DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/smmalloc")
