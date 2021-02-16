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

import configparser
import os
import random
import string

import docker
from jinja2 import Template

from duckiter.template.config_cfg import config_cfg as config_cfg_template
from duckiter.template.docker_file import dockerfile as docker_file_template


def get_django_project_name(project_path) -> str:
    """
    get project name

    :param project_path: path of project
    """
    # list of all files and dirs in root
    project_dirs = {}
    for r, d, f in os.walk(project_path):
        for file in f:
            project_dirs[file] = os.path.join(r, file)

    # get the path of settings.py file
    project_main_dir = str(project_dirs['settings.py'])

    return project_main_dir.split('/')[-2]


def get_project_server(project_path, project_name) -> str:
    """
    get project server ( runserver , gunicorn , daphne ,..... )
    it looks through requirements.txt file

    :param project_path: path of project
    :param project_name: name of django project
    """
    is_gunicorn = False
    is_daphne = False

    with open(project_path + "/requirements.txt", 'r') as file:
        for line in file:
            if 'gunicorn' in line:
                is_gunicorn = True
            if 'daphne' in line:
                is_daphne = True

    if is_gunicorn:
        return f'CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "{project_name}.wsgi"]'
    elif is_daphne:

        return f'CMD ["daphne","-b", "0.0.0.0", "-p","8000", "--access-log", "-","--proxy-headers", "{project_name}.asgi:application"]'
    else:
        return 'CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]'


def create_docker_configuration_file(
        config, project_name, project_path) -> None:
    """
    create config.cfg file that Dockerfile read settings from this

    :param project_path: path of project
    :param config: configuration that user entered
    :param project_name: name of django project
    """
    project_server = get_project_server(
        project_path=project_path,
        project_name=project_name)

    project_name = str(project_name)
    project_server = str(project_server)

    config_file = Template(config_cfg_template)
    config_file = config_file.render(
        project_name=project_name,
        python_version=config['python_version'],
        is_migration=config['is_migration'],
        project_server=project_server,
    )

    with open(project_path + '/config.cfg', 'w+') as file:
        file.write(config_file)


def create_dockerfile(project_path) -> None:
    """
    create dockerfile from config.cfg
    :param project_path: path of project
    """
    config = configparser.RawConfigParser()
    config.read(f'{project_path}/config.cfg')

    project_info = dict(config.items('project_info'))
    project_server = dict(config.items('project_server'))
    migrate = 'CMD ["python3","manage.py","migrate"]' if project_info['is_migration'] == 'True' else ""

    dockerfile = Template(docker_file_template)
    python_version = project_info['python_version']
    python_server = project_server['project_server']
    
    dockerfile = dockerfile.render(
        python_version=python_version,
        migrate=migrate,
        project_server=python_server,
    )

    with open(project_path + '/Dockerfile', 'w+') as file:
        file.write(dockerfile)


def generate_random_string() -> str:
    """
    create random string with 5 character
    """
    letter = string.ascii_lowercase
    random_string = ''.join(random.choice(letter) for i in range(5))
    return random_string
