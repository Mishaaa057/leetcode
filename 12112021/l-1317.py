# 1317. Convert Integer to the Sum of Two No-Zero Integers

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', type=int, nargs=1, help='Integer N')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser 


class Solution:
    def getNoZeroIntegers(self, n: int) -> list:
        a = 0
        
        while '0' in str(a) or '0' in str(n):
            a += 1
            n -= 1
        
        return [a, n]


def main():
	descr = f'''
{Fore.RED}{'=' * 70}{Fore.RESET}
{Fore.GREEN}
	# 1317. Convert Integer to the Sum of Two No-Zero Integers

Given an integer n. No-Zero integer is a positive integer which 
doesn't contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
It's guarateed that there is at least one valid solution. If 
there are many valid solutions you can return any of them.
{Fore.RESET}
{Fore.RED}{'=' * 70}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1317.py -n 2
	>>> [1,1]
{Fore.GREEN}
	Explanation: A = 1, B = 1. A + B = n and both A and B don't 
	contain any 0 in their decimal representation.
{Fore.RESET}
Example 2:
	$ python3 l-1317.py -n 11
	>>> [2,9]

Example 3:
	$ python3 l-1317.py -n 10000
	>>> [1,9999]

Example 4:
	$ python3 l-1317.py -n 69
	>>> [1,68]

Example 5:
	$ python3 l-1317.py -n 1010
	>>> [11,999]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.n:
		result = Solution().getNoZeroIntegers(args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()

