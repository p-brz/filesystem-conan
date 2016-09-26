from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "master")
username = os.getenv("CONAN_USERNAME", "paulobrizolara")
version  = "0.0.1-0a539a6"

class FilesystemTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "filesystem/%s@%s/%s" % (version, username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "bin")

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
