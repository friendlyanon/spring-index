cmake_minimum_required(VERSION 3.15)

project(CUtils)

set(root "source_subfolder/AI/Wrappers/CUtils")

add_library(CUtils STATIC
"${root}/SharedLibrary.c"
"${root}/SimpleLog.c"
"${root}/SimpleProfiler.cpp"
"${root}/Util.c"
"${root}/TimeUtil.cpp"
)

target_include_directories(CUtils PRIVATE "${root}" source_subfolder/rts)

include(GNUInstallDirs)

install(TARGETS CUtils EXPORT CUtilsConfig INCLUDES DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")
install(FILES
"${root}/SharedLibrary.h"
"${root}/SimpleLog.h"
"${root}/SimpleProfiler.h"
"${root}/Util.h"
"${root}/TimeUtil.h"
DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/CUtils")
install(DIRECTORY "${root}/bin/" TYPE BIN)
install(EXPORT CUtilsConfig NAMESPACE CUtils:: DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/CUtils")
