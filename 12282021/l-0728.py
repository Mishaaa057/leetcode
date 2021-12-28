# 728. Self Dividing Numbers

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-l', '--left', type=int, nargs=1, help='Left Integer')
	parser.add_argument('-r', '--right', type=int, nargs=1, help='Right Integer')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list:
        result = []
        for num in range(left, right + 1):
            if '0' not in str(num):
                is_self_dividing = True
                for el in str(num):
                    if num % int(el) != 0:
                        is_self_dividing = False
                        break
                if is_self_dividing:
                    result.append(num)
        
        return result


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit
it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0,
128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the
self-dividing numbers in the range [left, right].
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0728.py --left 1 --right 22
	>>> [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:
	$ python3 l-0728.py --left 47 --right 85
	>>> [48,55,66,77]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.left and args.right:
		result = Solution().selfDividingNumbers(args.left[0], args.right[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
