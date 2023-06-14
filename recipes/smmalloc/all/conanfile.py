import os

from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy, rmdir, get

required_conan_version = ">=2.0.0"


class SmMallocConan(ConanFile):
    name = "smmalloc"
    description = "Blazing fast memory allocator designed for video games"
    homepage = "https://github.com/SergeyMakeev/smmalloc"
    url = "https://github.com/friendlyanon/spring-index"
    license = "MIT"
    package_type = "static-library"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain"

    def export_sources(self):
        copy(self, "CMakeLists.txt", self.recipe_folder, self.export_sources_folder)

    def layout(self):
        cmake_layout(self)

    def validate(self):
        if self.settings.get_safe("compiler.cppstd"):
            check_min_cppstd(self, 17)

    def source(self):
        get(self, **self.conan_data["sources"][self.version],
            destination="source_subfolder", strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        CMake(self).install()
        rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "smmalloc")
        self.cpp_info.set_property("cmake_target_name", "smmalloc::smmalloc")
        self.cpp_info.libs = ["smmalloc"]
