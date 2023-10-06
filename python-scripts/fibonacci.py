#! /usr/bin/env python3


# accept an argument from the command line
# the input number, i.e., the position in the fib sequence
def get_input():
	number = input("Enter the position in the Fibonacci sequence: ")

	print(number)

	return int(number)


# calculate the fib number
def fib_num():
	# initiate the fib sequence
	a,b = 0,1

	for i in range(int(number)):
		a,b = b,a+b

	fibonacci_number = a


# print the output
def print_output():
	print(fibonacci_number)


# define main()
def main():
	
	# get the input
	input_num = get_input()
	
	print(input_num, "in main")

	# calcuate the fib number
#	fib_num()

	# print the output
#	print_output()



# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
	main()












