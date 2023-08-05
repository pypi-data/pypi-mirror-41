# grumbuild - A primitive build automation thingy
# Copyright (C) 2018-2019 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from typing import Optional, List

import os
import subprocess

from grumbuild.cmake_generator import CMakeGenerator, MakeCMakeGenerator


class CMakeProject:

    def __init__(self, builddir: str,
                 buildtype: str,
                 cc: Optional[str],
                 cxx: Optional[str],
                 extra_args: List[str],
                 generator: Optional[CMakeGenerator],
                 jobs: Optional[int]) -> None:
        self._builddir = builddir
        self._buildtype = buildtype
        self._cc = cc
        self._cxx = cxx
        self._extra_args = extra_args

        self._env = os.environ.copy()

        self._generator = generator or MakeCMakeGenerator()
        if jobs is not None:
            self._generator.set_jobs(jobs)

        if self._cc is not None:
            self._env["CC"] = self._cc

        if self._cxx is not None:
            self._env["CXX"] = self._cxx

        if not os.path.exists(builddir):
            os.mkdir(builddir)

    def print_info(self):
        print("BUILDDIR={}".format(self._builddir))

        if self._cc is not None:
            print("CC={}".format(self._cc))

        if self._cxx is not None:
            print("CXX={}".format(self._cxx))

    def configure(self) -> None:
        args = ["cmake", "..",
                "-G", self._generator.name,
                "-DCMAKE_BUILD_TYPE=" + self._buildtype,
                "-DWARNINGS=ON",
                "-DWERROR=ON",
                *self._extra_args]
        subprocess.check_call(args, env=self._env, cwd=self._builddir)

    def build(self, targets: List[str] = []) -> None:
        args = [self._generator.exe] + self._generator.args + targets
        subprocess.check_call(args, cwd=self._builddir)

    def test(self):
        if os.path.exists(os.path.join(self._builddir, "CTestTestfile.cmake")):
            subprocess.check_call([self._generator.exe] + self._generator.args + ["test"],
                                  env=self._env, cwd=self._builddir)
        else:
            print("no CTestTestfile.cmake, skipping test step")


# EOF #
