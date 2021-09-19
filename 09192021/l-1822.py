# 1822. Sign of the Product of an Array

from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', metavar='n',
		nargs='+', type=int, help='Integer array')
	parser.add_argument('--description', '-d', action='store_true',
		help='Show description')
	parser.add_argument('--example', '-e', action='store_true',
		help='Show example')

	return parser 


class Solution:
    def arraySign(self, nums):
        number = 1
        
        for el in nums:
            number = number * el
        
        if number > 0:
            return 1
        elif number < 0:
            return -1
        else:
            return 0


def Main():
	descr = f'''
{Fore.RED}============================================================{Fore.RESET}
	{Fore.GREEN}# 1822. Sign of the Product of an Array

There is a function signFunc(x) that returns:
	1 if x is positive.
	-1 if x is negative.
	0 if x is equal to 0.

You are given an integer array nums. 
Let product be the product of all values in the array nums.{Fore.RESET}
{Fore.RED}============================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 --nums -1 -2 -3 -4 3 2 1
	>>> 1
	{Fore.GREEN}Explanation: The product of all values in 
	the array is 144, and signFunc(144) = 1{Fore.RESET}

Example 2:
	$ python3 --nums 1 5 0 2 -3
	>>> 0
	{Fore.GREEN}Explanation: The product of all values in 
	the array is 0, and signFunc(0) = 0{Fore.RESET}

Example 3:
	$ python3 --nums -1 1 -1 1 -1
	>>> -1
	{Fore.GREEN}Explanation: The product of all values in 
	the array is -1, and signFunc(-1) = -1{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().arraySign(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()