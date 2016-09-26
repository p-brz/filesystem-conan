from conans import ConanFile, tools
import os
from os import path

class FilesystemConan(ConanFile):
    name = "filesystem"
    version = "0.0.1-0a539a6"
    license = "BSD-3-Clause"
    url = "https://github.com/paulobrizolara/filesystem-conan"

    REPO = "https://github.com/wjakob/filesystem.git"
    COMMIT = "0a539a6"
    GIT_DIRNAME = name

    def source(self):
        # Clone the repository
        self.run("git clone %s %s" % (self.REPO, self.GIT_DIRNAME))
        self.run("git checkout %s" % self.COMMIT, cwd=self.GIT_DIRNAME)

    def package(self):
        self.copy("*", path.join("include", "filesystem"), path.join(self.GIT_DIRNAME, 'filesystem'), keep_path=True)

    def package_info(self):
        self.cpp_info.cppflags = ["-std=c++11"]
