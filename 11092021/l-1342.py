# 1342. Number of Steps to Reduce a Number to Zero

from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--num', nargs=1, metavar='n', type=int, help='Some integer num')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num != 0:
            # If the number is even
            if (num % 2) == 0:
                num = num // 2
            # If number not even
            else:
                num -= 1
            counter += 1
        return counter


def main():
	descr = f'''
{Fore.RED}================================================{Fore.RESET}
{Fore.GREEN}
	# 1342. Number of Steps to 
	  Reduce a Number to Zero

Given an integer num, return the number of 
steps to reduce it to zero.

In one step, if the current number is even, 
you have to divide it by 2, otherwise, 
you have to subtract 1 from it.
{Fore.RESET}
{Fore.RED}================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1342.py --num 14
	>>> 6
{Fore.GREEN}	
	Explanation: 
		Step 1) 14 is even; divide by 2 and obtain 7. 
		Step 2) 7 is odd; subtract 1 and obtain 6.
		Step 3) 6 is even; divide by 2 and obtain 3. 
		Step 4) 3 is odd; subtract 1 and obtain 2. 
		Step 5) 2 is even; divide by 2 and obtain 1. 
		Step 6) 1 is odd; subtract 1 and obtain 0.
{Fore.RESET}
Example 2:
	$ python3 l-1342.py  --num 8
	>>> 4
{Fore.GREEN}
	Explanation: 
		Step 1) 8 is even; divide by 2 and obtain 4. 
		Step 2) 4 is even; divide by 2 and obtain 2. 
		Step 3) 2 is even; divide by 2 and obtain 1. 
		Step 4) 1 is odd; subtract 1 and obtain 0.
{Fore.RESET}
Example 3:
	$ python3 l-1342.py --num 123
	>>> 12
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.num:
		result = Solution().numberOfSteps(args.num[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()


	