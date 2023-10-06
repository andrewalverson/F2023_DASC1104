#! /usr/bin/env python3


# accept an argument from the command line
# the input number, i.e., the position in the fib sequence
def get_input():
	number = input("Enter the position in the Fibonacci sequence: ")

	return int(number)


# calculate the fib number
def calc_fib(n):
	# initiate the fib sequence
	a,b = 0,1

	for i in range(n):
		a,b = b,a+b

	fibonacci_number = a

	return fibonacci_number	


# print the output
def print_output(user_input, output):
	print('The Fibonacci number for', user_input, 'is', output)


# define main()
def main():
	
	# get the input
	input_num = get_input()
	
	# calcuate the fib number
	fib_number = calc_fib(input_num)

	# print the output
	print_output(input_num, fib_number)








# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
	main()












