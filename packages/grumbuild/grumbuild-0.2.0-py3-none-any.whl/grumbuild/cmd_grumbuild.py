# grumbuild - A primitive build automation thingy
# Copyright (C) 2018 Ingo Ruhnke <grumbel@gmail.com>
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


from typing import List, Optional

import argparse
import fnmatch
import os
import re
import sys
import time
import yaml

from grumbuild.cmake_project import CMakeProject
from grumbuild.cmake_generator import CMakeGenerator, MakeCMakeGenerator


GLOB_PATTERN_RX = re.compile(r"[\*\?\[\]]")


class BuildResult:

    def __init__(self):
        self.start_time: Optional[float] = None
        self.finish_time: Optional[float] = None
        self.error: Optional[str] = None

    def log_start(self):
        self.start_time = time.time()

    def log_finish(self, error):
        self.finish_time = time.time()
        self.error = error

    def duration(self) -> float:
        assert self.finish_time is not None
        assert self.start_time is not None

        return self.finish_time - self.start_time


def is_glob_pattern(text):
    return bool(GLOB_PATTERN_RX.search(text))


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Meta build tool")
    parser.add_argument("BUILD", nargs="*",
                        help="BUILD that should be build or glob pattern")

    parser.add_argument('-f', '--file', metavar='FILE', type=str, default=".grumbuild.yml",
                        help="Load build definitions from FILE")
    parser.add_argument('-l', '--list', action='store_true', default=False,
                        help="List available builds")
    parser.add_argument('-j', '--jobs', metavar="JOBS", type=int,
                        help="Number of parallel runs")
    parser.add_argument('-k', '--keep-going', action='store_true', default=False,
                        help="Continue to build on failure")

    parser.add_argument('-c', '--configure', action='store_true', default=False,
                        help="Run the configure stage")
    parser.add_argument('-b', '--build', action='store_true', default=False,
                        help="Run the build stage")
    parser.add_argument('-t', '--test', action='store_true', default=False,
                        help="Run the test stage")
    parser.add_argument('-T', '--target', nargs='+', metavar="TARGET", default=[],
                        help='Build TARGET')

    return parser.parse_args(args)


def main(argv: List[str]) -> None:
    args = parse_args(sys.argv[1:])

    if os.path.exists(args.file):
        with open(args.file) as fin:
            builds_definition = yaml.load(fin)
    else:
        builds_definition = {'default': {'buildtype': 'Release'}}

    if args.list:
        for build in sorted(builds_definition.keys()):
            print(build)
    else:
        if args.BUILD == []:
            build_items = builds_definition
        else:
            build_items = {}
            for key in args.BUILD:
                if is_glob_pattern(key):
                    for k, v in builds_definition.items():
                        if fnmatch.fnmatch(k, key):
                            build_items[k] = v
                else:
                    build_items[key] = builds_definition[key]

        build_times = {}
        for builddir, build in build_items.items():
            build_times[builddir] = BuildResult()
            build_times[builddir].log_start()
            try:
                project = CMakeProject(
                    "build." + builddir,
                    build["buildtype"],
                    build["compiler"][0] if ("compiler" in build) else None,
                    build["compiler"][1] if ("compiler" in build) else None,
                    build["args"] if ("args" in build) else [],
                    CMakeGenerator.from_string(build["generator"]) if "generator" in build
                    else MakeCMakeGenerator(),
                    args.jobs)

                project.print_info()

                if not args.configure and not args.build and not args.test and not args.target:
                    project.configure()
                    project.build()
                    project.test()
                else:
                    if args.configure:
                        project.configure()
                    if args.build:
                        project.build()
                    if args.test:
                        project.test()
                    if args.target:
                        project.build(args.target)

            except Exception as err:
                if args.keep_going:
                    build_times[builddir].log_finish(err)
                else:
                    raise
            else:
                build_times[builddir].log_finish(None)

        print()
        print("Summary")
        for builddir, result in build_times.items():
            if result.error is None:
                print("  {:24}   ok   {:>8.2f}secs".format(builddir, result.duration()))
            else:
                print("  {:24}  fail  {:>8.2f}secs  {}".format(builddir, result.duration(), result.error))


def main_entrypoint():
    main(sys.argv)


# EOF #
