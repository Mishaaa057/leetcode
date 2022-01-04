# 1009. Complement of Base 10 Integer

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', type=int, nargs=1, help='Integer N')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_num = bin(n)[2:]
        result_bin = ''
        for el in str(bin_num):
            if el == '1':
                result_bin += '0'
            else:
                result_bin += '1'
        
        result_num = int(result_bin, 2)
        return result_num
        


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 1009. Complement of Base 10 Integer

The complement of an integer is the integer you get when you flip
all the 0's to 1's and all the 1's to 0's in its binary
representation.

For example, The integer 5 is "101" in binary and its complement is
"010" which is the integer 2.
Given an integer n, return its complement.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1009.py -n 5
	>>> 2
{Fore.GREEN}
	Explanation: 5 is "101" in binary, with complement "010" in
		binary, which is 2 in base-10.
{Fore.RESET}
Example 2:
	$ python3 l-1009.py -n 7
	>>> 0
{Fore.GREEN}
	Explanation: 7 is "111" in binary, with complement "000" in
		binary, which is 0 in base-10.
{Fore.RESET}
Example 3:
	$ python3 l-1009.py -n 10
	>>> 5
{Fore.GREEN}
	Explanation: 10 is "1010" in binary, with complement "0101"
		in binary, which is 5 in base-10.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.n:
		result = Solution().bitwiseComplement(args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
