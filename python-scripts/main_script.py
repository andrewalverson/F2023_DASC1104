#!/usr/bin/env python3

import say_hello


def main():
	name = input("Enter your name: ")
	say_hello.hello_statement(name)


# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
	main()
