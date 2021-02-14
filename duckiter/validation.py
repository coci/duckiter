from os import path
import sys

from colored import fg, bg, attr
import docker
from docker.errors import DockerException


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
					"%s%s [ WARNING !!! ] %s this is not valid django project, run '--init' inside django project." % (
						fg(15), bg(1), attr(0)))
				sys.exit()
	print(" [ 1/6 ] check project validity ......%s[passed] %s" % (fg(2), attr(0)))

	if not path.exists(f'{project_path}/requirements.txt'):
		print(
			"%s%s [ WARNING !!! ] %s There isn't any 'requirements.txt' file in current path, please provide for further steps." % (
				fg(15), bg(1), attr(0)))
		sys.exit()

	print(" [ 2/6 ] check requirements.txt validty ......%s[passed] %s" % (fg(2), attr(0)))


def docker_engine_status_checker() -> None:
	"""
		check is docker engine already up
	"""

	try:
		client = docker.from_env()
	except DockerException:
		print("%s%s [ WARNING !!! ] %s It seems your docker engine doesn't run, please run the Docker engine." % (
			fg(15), bg(1), attr(0)))
		sys.exit()
	print(" [ 1/3 ] check docker engine status ......%s[passed]%s" % (fg(2), attr(0)))


def check_dockerfile(project_path):
	"""
		check if project path has Dockerfile ( for build process )
	:param project_path: path of project
	"""
	if path.isdir(project_path):
		if path.exists(project_path):
			if not path.exists(f'{project_path}/Dockerfile'):
				print(
					"%s%s [ WARNING !!! ] %s this is not valid django project, run '--init' inside django project." % (
						fg(15), bg(1), attr(0)))
				sys.exit()
	print(" [ 2/3 ] check project validity ......%s[passed] %s" % (fg(2), attr(0)))
