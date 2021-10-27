# 231. Power of Two


import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--number', type=int, nargs=1, help='Integer n')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 2
        k = 1
        if n == 1 or n == 2:
            return True
        
        while x < n:
            x = 2 ** k
            k += 1
            if x == n:
                return True
        return False


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 231. Power of Two

Given an integer n, return true if it is a power
of two. Otherwise, return false.

An integer n is a power of two, if there 
exists an integer x such that n == 2x?
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0231.py --number 1
	>>> True
{Fore.GREEN}	
	Explanation: 20 = 1
{Fore.RESET}
Example 2:
	$ python3 l-0231.py --number 16
	>>> True
{Fore.GREEN}
	Explanation: 24 = 16
{Fore.RESET}
Example 3:
	$ python3 l-0231.py --number 3
	>>> False

Example 4:
	$ python3 l-0231.py --number 4
	>>> True

Example 5:
	$ python3 l-0231.py --number 5
	>>> False
	''' 

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.number:
		result = Solution().isPowerOfTwo(args.number[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()