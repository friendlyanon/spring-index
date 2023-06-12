import os

from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy, rmdir, get, export_conandata_patches, apply_conandata_patches

required_conan_version = ">=2.0.0"


class CUtilsConan(ConanFile):
    name = "cutils"
    description = "CUtils wrapper"
    homepage = "https://github.com/beyond-all-reason/spring"
    url = "https://github.com/friendlyanon/spring-index"
    license = "GPL-2.0-or-later"
    package_type = "static-library"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain"

    def export_sources(self):
        export_conandata_patches(self)
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
        apply_conandata_patches(self)
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        CMake(self).install()
        rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "CUtils")
        self.cpp_info.set_property("cmake_target_name", "CUtils::CUtils")
        self.cpp_info.libs = ["CUtils"]
