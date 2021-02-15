# -*- coding: utf-8 -*-
#
# Copyright (C) 2021- Soroush Safari <mr.safarii1992@gmail.com>
#
# This file is part of duckiter.
#
# duckiter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# duckiter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with grest.  If not, see <http://www.gnu.org/licenses/>.
#

import argparse

from duckiter.duckiter import Duckiter


def main():
    duckiter_instance = Duckiter()

    my_parser = argparse.ArgumentParser(
        description='List the content of a folder')
    my_parser.add_argument('--init',
                           action='store_true',
                           help='initialize dockerfile in your project')

    my_parser.add_argument('--build', '-b',
                           action='store_true',
                           help='build from docker file')

    args = my_parser.parse_args()

    if args.init:
        duckiter_instance.initialize()

    if args.build:
        duckiter_instance.build()
