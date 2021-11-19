# 67. Add Binary

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-a', type=str, metavar='"N"', nargs=1, help='Binary string A')
	parser.add_argument('-b', type=str, metavar='"N"', nargs=1, help='Binary string B')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return (format((int(a, 2) + int(b, 2)), 'b'))


def main():
	descr = f'''
{Fore.RED}================================================{Fore.RESET}
{Fore.GREEN}
	# 67. Add Binary

Given two binary strings a and b, return their 
sum as a binary string.
{Fore.RESET}
{Fore.RED}================================================{Fore.RESET}
	'''
	
	example = '''
Example 1:
	$ python3 l-0067.py -a "11" -b "1"
	>>> "100"

Example 2:
	$ python3 l-0067.py -a "1010" -b "1011"
	>>> "10101"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.a and args.b:
		result = Solution().addBinary(args.a[0], args.b[0])
		print(f'"{result}"')

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
	