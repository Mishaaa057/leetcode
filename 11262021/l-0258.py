# 258. Add Digits

import argparse 
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--num', type=int, nargs=1, help='Integer num')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            n = 0
            for el in str(num):
                n += int(el)
            
            num = n
        
        return num


def main():
	descr = f'''
{Fore.RED}====================================================={Fore.RESET}
{Fore.GREEN}
	# 258. Add Digits

Given an integer num, repeatedly add all its digits 
until the result has only one digit, and return it.
{Fore.RESET}
{Fore.RED}====================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0258.py --num 38
	>>> 2
{Fore.GREEN}
	Explanation: The process is
	38 --> 3 + 8 --> 11
	11 --> 1 + 1 --> 2 
	Since 2 has only one digit, return it.
{Fore.RESET}
Example 2:
	$ python3 l-0258.py --num 0
	>>> 0
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.num:
		result = Solution().addDigits(args.num[0])
		print(result)

	elif args.description:	
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
