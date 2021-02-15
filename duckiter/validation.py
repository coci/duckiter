import sys
from os import path

import docker
from docker.errors import DockerException
from rich import print


def pre_validation(project_path):
    """
            check if project_path is valid path ( contain django project)
    :param project_path: path of project
    """

    # check project_path status ( is valid django project)
    if path.isdir(project_path):
        if path.exists(project_path):
            if not path.exists(f'{project_path}/manage.py'):
                print(
                    "bold red][ WARNNING !!!! ][/bold red] this is not valid django project, run '--init' inside django project.")
                sys.exit()
    print("[ 1/6 ] check project validity ......[bold green][ passed ][/bold green]")

    if not path.exists(f'{project_path}/requirements.txt'):
        print("[bold red][ WARNNING !!!! ][/bold red] There isn't any 'requirements.txt' file in current path, please provide for further steps.")
        sys.exit()

    print(" [ 2/6 ] check requirements.txt validty ......[bold green][ passed ][/bold green]")


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
    if path.isdir(project_path):
        if path.exists(project_path):
            if not path.exists(f'{project_path}/Dockerfile'):
                print(
                    "[bold red][ WARNNING !!!! ][/bold red] this is not valid django project, run '--init' inside django project.")
                sys.exit()
    print(" [ 2/3 ] check project validity ......[bold green][ passed ][/bold green]")
