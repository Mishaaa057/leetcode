# 415. Add Strings


import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n1', '--num1', nargs=1, type=int, metavar='n', help='Number 1')
	parser.add_argument('-n2', '--num2', nargs=1, type=int, metavar='n', help='Number 2')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


def main():
	descr = f'''
{Fore.RED}=================================================================={Fore.RESET}
{Fore.GREEN}
		# 415. Add Strings
Given two non-negative integers, num1 and num2 represented 
as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in 
library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.
{Fore.RESET}
{Fore.RED}=================================================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0415.py --num1 "11" --num2 "123"
	>>> 134

Example 2:
 	$ python3 l-0415.py --num1 "456" --num2 "77"
	>>> 533

Example 3:

	$ python3 l-0415.py --num1 "0" --num2 "0"
	>>> 0
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.num1 and args.num2:
		result = Solution().addStrings(args.num1[0], args.num2[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
