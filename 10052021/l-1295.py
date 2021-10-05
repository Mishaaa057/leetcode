# 1295. Find Numbers with Even Number of Digits


from colorama import Fore as F
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', metavar='n', help='Number array' )
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def findNumbers(self, nums: list) -> int:
        result = 0
        for el in nums:
            if len(str(el)) % 2 == 0:
                result += 1
        return result



def main():
	descr = f'''
{F.RED}====================================================================={F.RESET}
{F.GREEN}
	# 1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain 
an even number of digits.
{F.RESET}
{F.RED}====================================================================={F.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1295.py --nums 12 345 2 6 7896
	>>> 2
{F.GREEN}
	Explanation: 
	12 contains 2 digits (even number of digits). 
	345 contains 3 digits (odd number of digits). 
	2 contains 1 digit (odd number of digits). 
	6 contains 1 digit (odd number of digits). 
	7896 contains 4 digits (even number of digits). 
	Therefore only 12 and 7896 contain an even number of digits.
{F.RESET}
Example 2:
	$ python3 l-1295.py --nums 555 901 482 1771
	>>> 1 
{F.GREEN}
	Explanation: 
	Only 1771 contains an even number of digits.
{F.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().findNumbers(args.nums)
		print(result)

	elif args.description:
		print(descr)
	
	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
