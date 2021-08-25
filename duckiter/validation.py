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

import sys
import os

import docker
from docker.errors import DockerException
from rich import print


def pre_validation(project_path):
    """
    check if project_path is valid path ( contain django project)

    :param project_path: path of project
    """

    # check project_path status ( is valid django project)
    REQUIREMENTS_AUTO_CREATED = False

    if not os.path.exists(os.path.join(project_path, 'manage.py')):
        print("[bold red][ WARNNING !!!! ][/bold red] this is not valid django project, run '--init' inside django project.")
        sys.exit()
    print("[ 1/6 ] check project validity ......[bold green][ passed ][/bold green]")

    if not os.path.exists(os.path.join(project_path, 'requirements.txt')):
        venv_path = ''
    
        for r, d, f in os.walk(project_path):
            for file in f:
                if file.lower() == 'pyvenv.cfg':
                    path_seprator, venv_path = '/' if '/' in r else '\\', r
        
        if not venv_path:
            print("[bold red][ WARNNING DEBUG !!!! ][/bold red] There isn't any 'requirements.txt' file or virtual environment in current path, please provide for further steps.")
            sys.exit()

        print(
            "[bold blue][ ACTION ][/bold blue] requirements.txt file not found,"
            "creating this file automatically through your virutal environment"
            " ({})".format(venv_path.split(path_seprator)[-1])
        )

        MODULES = []
        if os.name == 'nt':
            venv_path = os.path.join(
                venv_path, 'Lib', 'site-packages')
        else:
            venv_path = os.path.join(
                venv_path, 'lib', [i for i in os.walk(os.path.join(venv_path, 'lib'))][0][1][0], 'site-packages')

        for i in os.listdir(venv_path):
            if os.path.isdir(os.path.join(venv_path, i)):
                if (
                    not i.startswith(('pip', 'setuptools', 'wheel')) and
                    i not in ['_distutils_hack', 'pkg_resources'] and
                    i.endswith('.dist-info')
                ):
                    MODULES.append('=='.join(i.split('.dist-info')[0].split('-')))
        
        with open('requirements.txt', 'a') as requirements_file:
            for MODULE in MODULES:
                requirements_file.write(MODULE+'\n')
            requirements_file.close()
            REQUIREMENTS_AUTO_CREATED = True

    print(" [ 2/6 ] {}[bold green][ passed ][/bold green]".format(
        'check requirements.txt validty...' if not REQUIREMENTS_AUTO_CREATED else
        'The requirements.txt file is created automatically for your project and will be used in project dockerizing.'
    ))


def docker_engine_status_checker() -> None:
    """
    check is docker engine already up
    """

    try:
        docker.from_env()
    except DockerException:
        print("[bold red][ WARNNING !!!! ][/bold red] It seems your docker engine doesn't run, please run the Docker engine.")
        sys.exit()
    print(" [ 1/3 ] check docker engine status ......[bold green][ passed ][/bold green]")


def check_dockerfile(project_path):
    """
    check if project path has Dockerfile ( for build process )
    
    :param project_path: path of project
    """
    if not os.path.exists(os.path.join(project_path, 'Dockerfile')):
        print("[bold red][ WARNNING !!!! ][/bold red] this is not valid django project, run '--init' inside django project.")
        sys.exit()
    print(" [ 2/3 ] check project validity ......[bold green][ passed ][/bold green]")
