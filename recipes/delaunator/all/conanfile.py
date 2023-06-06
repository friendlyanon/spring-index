import os

from conan import ConanFile
from conan.tools.files import copy, get
from conan.tools.build import check_min_cppstd

required_conan_version = ">=2.0.0"


class DelaunatorConan(ConanFile):
    name = "delaunator-cpp"
    description = "A really fast C++ library for Delaunay triangulation of 2D points"
    homepage = "https://github.com/friendlyanon/delaunator-cpp"
    url = "https://github.com/friendlyanon/spring-index"
    license = "MIT"
    package_type = "header-library"
    settings = "compiler"
    no_copy_source = True

    def package_id(self):
        self.info.clear()

    def validate(self):
        if self.settings.get_safe("compiler.cppstd"):
            check_min_cppstd(self, 17)

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def package(self):
        copy(self, "*.hpp", src=os.path.join(self.source_folder, "include"), dst=os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "delaunator")
        self.cpp_info.set_property("cmake_target_name", "delaunator::delaunator")
