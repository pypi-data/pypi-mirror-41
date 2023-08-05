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


from typing import List

from abc import ABC, abstractmethod


class CMakeGenerator(ABC):

    @staticmethod
    def from_string(text: str) -> 'CMakeGenerator':
        if text == "ninja" or text == "Ninja":
            return NinjaCMakeGenerator()
        elif text == "make" or text == "Unix Makefiles":
            return MakeCMakeGenerator()
        else:
            raise Exception("Unknown generator type: '{}'".format(text))

    def __init__(self):
        self._verbose = True
        self._jobs = 1

    def set_verbose(self, verbose: bool) -> None:
        self._verbose = verbose

    def set_jobs(self, jobs: int) -> None:
        self._jobs = jobs

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def exe(self) -> str:
        pass

    @property
    @abstractmethod
    def args(self) -> List[str]:
        pass


class MakeCMakeGenerator(CMakeGenerator):

    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Unix Makefiles"

    @property
    def exe(self) -> str:
        return "make"

    @property
    def args(self) -> List[str]:
        args = []
        if self._verbose:
            args.append("VERBOSE=1")

        args.append("CTEST_OUTPUT_ON_FAILURE=1")

        args.append("-j")
        args.append(str(self._jobs))

        return args


class NinjaCMakeGenerator(CMakeGenerator):

    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Ninja"

    @property
    def exe(self) -> str:
        return "ninja"

    @property
    def args(self) -> List[str]:
        args = []
        if self._verbose:
            args.append("-v")

        args.append("-j")
        args.append(str(self._jobs))

        return args


# EOF #
