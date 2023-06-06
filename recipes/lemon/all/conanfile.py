import os

from conan import ConanFile
from conan.tools.files import copy, get
from conan.tools.build import check_min_cppstd

required_conan_version = ">=2.0.0"


class LemonConan(ConanFile):
    name = "lemon"
    description = "A Library for Efficient Modeling and Optimization in Networks"
    homepage = "https://github.com/friendlyanon/lemon"
    url = "https://github.com/friendlyanon/spring-index"
    license = "BSL-1.0"
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
        copy(self, "*", src=os.path.join(self.source_folder, "include"), dst=os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "lemon")
        self.cpp_info.set_property("cmake_target_name", "lemon::lemon")
