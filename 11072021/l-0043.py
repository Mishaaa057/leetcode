# 43. Multiply Strings

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n1','--num1', type=str, nargs=1, help='Non negative integer 1 represeted as string')
	parser.add_argument('-n2','--num2', type=str, nargs=1, help='Non negative integer 2 represeted as string')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


# Get integer from string without int() function
def get_num(string_num):
    new_num = 0
    for index, el in enumerate(string_num):
        for num in range(10):
            if str(num) == el:
                r = num *  (10 ** len(string_num[index + 1:]))
                new_num  += r
    return new_num


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
    	# Get integers from strings num1 and num2
        num1 = get_num(num1)
        num2 = get_num(num2)   
        
        return str(num1 * num2)


def main():
	descr = f'''
{Fore.RED}======================================================{Fore.RESET}
{Fore.GREEN}
	# 43. Multiply Strings

Given two non-negative integers num1 and num2 
represented as strings, return the product of 
num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger 
library or convert the inputs to integer directly.
{Fore.RESET}
{Fore.RED}======================================================{Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0043.py --num1 "2" --num2 "3"
	>>> "6"

Example 2:
	$ python3 l-0043.py --num1 "123" --num2 "456"
	>>> "56088"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.num1 and args.num2:
		result = Solution().multiply(args.num1[0], args.num2[0])
		print(f'"{result}"')

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__ == '__main__':
	main()
