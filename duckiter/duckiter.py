import os
import pathlib
from threading import Thread
from time import sleep

import docker
from rich import print
from rich.console import Console

from duckiter.config import get_config
from duckiter.utility import (create_docker_configuration_file,
                              create_dockerfile, get_django_project_name,
                              random_string)
from duckiter.validation import (check_dockerfile,
                                 docker_engine_status_checker, pre_validation)


class Duckiter:
    def __init__(self):
        self.__project_path = os.getcwd()
        self.__MODULE_PATH = str(pathlib.Path(__file__).resolve().parent)
        self.__docker_client = None
        self.__project_name = ''
        self.__config = {}
        self.__project_name = get_django_project_name(
            project_path=self.__project_path)

    def initialize(self):
        pre_validation(project_path=self.__project_path)
        print("[bold green][ INITIALIZING ][/bold green]")

        print("[ 3/6 ] getting project name ......[bold green][ passed ][/bold green]")

        self.__config = get_config()
        print("[ 4/6 ] getting configuration ......[bold green][ passed ][/bold green]")

        create_docker_configuration_file(
            config=self.__config,
            project_name=self.__project_name,
            project_path=self.__project_path)
        print(
            "[ 5/6 ] creating configuration file ......[bold green][ passed ][/bold green]")

        create_dockerfile(project_path=self.__project_path)
        print("[ 6/6 ] creating Dockerfile ......[bold green][ passed ][/bold green]")
        print(
            "[bold green][ NOTE ][/bold green] if there is gunicorn or daphne in your requirements.txt, Duckiter run your project with them"
            ", else your project will be run with runserver.")

        print("[bold green][ NOTE ][/bold green] if you didn't provide --build, you can edit Dockerfile or config.cfg and then run --build .")

    def build(self):
        self.__project_path = os.getcwd()

        docker_engine_status_checker()
        check_dockerfile(project_path=self.__project_path)

        print("[bold green][ BUILDING IMAGE ][/bold green]")
        print("it is going to take a while, please be patient...")

        self.__image_name = self.__project_name + "-" + random_string()
        self.__state = True

        create_image_thread = Thread(target=self.__build)
        create_image_thread.start()

        console = Console()
        with console.status("[bold green]Building image .....", spinner='point') as status:
            while self.__state:
                sleep(0.1)

        print("\n")
        print(" [ 3/3 ] creating image ......[bold green][ passed ][/bold green]")
        print("[bold green][ NOTE ][/bold green] you can run your image :")
        print(f'docker run -d -p 8000:8000 {self.__image_name}')
        print("you can hit '127.0.0.1:8000' in your browser.")

    def __build(self):
        client = docker.from_env()
        client.images.build(
            path=self.__project_path,
            tag=self.__image_name,
            rm=True,
            forcerm=True)
        self.__state = False
