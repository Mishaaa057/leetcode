# 476. Number Complement

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--num', type=int, nargs=1, help='an Integer')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def findComplement(self, num: int) -> int:
        n = bin(num)
        new = ''
        for index, el in enumerate(n):
            if index != 0:
                if el == '1':
                    new += '0'
                elif el == '0':
                    new += '1'
                else:
                    new += el
            else:
                new += el
        
        return int(new, 2)


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 476. Number Complement

The complement of an integer is the integer you get when you flip
all the 0's to 1's and all the 1's to 0's in its binary
representation.

	For example, The integer 5 is "101" in binary and its complement
	is "010" which is the integer 2.

Given an integer num, return its complement.
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0476.py --num 5
	>>> 2
{Fore.GREEN}
	Explanation: The binary representation of 5 is 101 (no leading zero
	bits), and its complement is 010. So you need to output 2.
{Fore.RESET}
Example 2:
	$ python3 l-0476.py --num 1
	>>> 0
{Fore.GREEN}
	Explanation: The binary representation of 1 is 1 (no leading zer
	 bits), and its complement is 0. So you need to output 0.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.num:
		result = Solution().findComplement(args.num[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
