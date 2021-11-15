# 509. Fibonacci Number

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', type=int, nargs=1, help='An integer n')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser


class Solution:
    def fib(self, n: int) -> int:
        fib_list = [0, 1, 2, 3]
        if n == 0:
            return 0
        
        while len(fib_list) < n:
            x = fib_list[len(fib_list) - 1]
            z = fib_list[len(fib_list) - 2]
            
            fib_list.append(x + z)
        
        if n > 1:
            return fib_list[n - 1]
        else:
            return fib_list[n]


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) 
form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two 
preceding ones, starting from 0 and 1. 
Given n, calculate F(n).
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0509.py -n 2
	>>> 1
{Fore.GREEN}
	Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
{Fore.RESET}
Example 2:
	$ python3 l-0509.py -n 3
	>>> 2
{Fore.GREEN}
	Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
{Fore.RESET}
Example 3:
	$ python3 l-0509.py -n 4
	>>> 3
{Fore.GREEN}
	Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.n:
		result = Solution().fib(args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()