# 263. Ugly Number

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', type=int, nargs=1, help='Number')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 



class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        
        while True:
            if n % 2 == 0:
                n = n // 2
            
            elif n % 3 == 0:
                n = n // 3
                
            elif n % 5 == 0:
                n = n // 5
            
            else:
                break

        return n == 1


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 263. Ugly Number

An ugly number is a positive integer whose prime factors are
limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0253.py -n 6
	>>> True
{Fore.GREEN}
	Explanation: 6 = 2 × 3
{Fore.RESET}
Example 2:
	$ python3 l-0253.py -n 1
	>>> True
{Fore.GREEN}
	Explanation: 1 has no prime factors, therefore all of its 
		prime factors are limited to 2, 3, and 5.
{Fore.RESET}
Example 3:
	$ python3 l-0253.py -n 14
	>>> False
{Fore.GREEN}
	Explanation: 14 is not ugly since it includes the prime factor 7.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.n:
		result = Solution().isUgly(args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()


