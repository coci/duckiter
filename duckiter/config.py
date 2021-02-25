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

def get_config() -> dict:
    """
    get config from user ( CLI )

    """
    print("please enter python version that you need insert in your Docker. Exp : ( 3.9-alpine or 3.9 )")
    python_version = input(
        "( blank will consider as 3.8-alpine ) : ")

    python_version = python_version if python_version else '3.8'

    is_migration = input(
        "Do you want add 'python manage.py migrate' in your docker file ? (y/n) : ")

    is_migration = True if is_migration == 'y' else False

    config = {
        'python_version': python_version,
        'is_migration': is_migration,

    }
    return config
