import argparse

from duckiter.duckiter import Duckiter


def main():
	duckiter_instance = Duckiter()

	my_parser = argparse.ArgumentParser(description='List the content of a folder')
	my_parser.add_argument('--init',
						   action='store_true',
						   help='initialize dockerfile in your project')

	my_parser.add_argument('-build', '-b',
						   action='store_true',
						   help='build from docker file')

	args = my_parser.parse_args()

	if args.init:
		duckiter_instance.initialize()

	if args.build:
		duckiter_instance.build()
