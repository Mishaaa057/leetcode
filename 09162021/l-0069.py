# 69. Sqrt(x)


from colorama import Fore
from math import sqrt
import argparse


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-x',  nargs=1, type=int, metavar='n', help='Some Number')
	parser.add_argument('--description', '-d', action='store_true',
		help='Show description')
	parser.add_argument('--example', '-e', action='store_true',
		help='Show example')

	return parser 


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))


def Main():
	descr = f'''
{Fore.RED}================================================================{Fore.RESET}
	{Fore.GREEN}	# 69. Sqrt(x)
	Given a non-negative integer x, compute and return 
	the square root of x.

	Since the return type is an integer, the decimal 
	digits are truncated, and only the integer part of 
	the result is returned.{Fore.RESET}
{Fore.RED}================================================================{Fore.RESET}
		'''

	example = '''
Example 1:
	$ python3 l-0069.py -x 4
	>>> 2

Example 2:
	$ python3 l-0069.py -x 8
	>>> 2
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.x:
		
		result = Solution().mySqrt(args.x[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__ == '__main__':
	Main()