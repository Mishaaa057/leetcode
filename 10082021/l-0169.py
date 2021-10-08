# 169. Majority Element


import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Nums array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def majorityElement(self, nums: list) -> int:
        dct = {}
        
        for el in nums:
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
            
        for key in dct:
            if dct[key] > len(nums) / 2:
                return key


def main():
	descr = f'''
{Fore.RED}=========================================================={Fore.RESET}
{Fore.GREEN}
	#  169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than 
⌊n / 2⌋ times. You may assume that the majority element 
always exists in the array.
{Fore.RESET}
{Fore.RED}=========================================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0169.py --nums 3 2 3
	>>> 3

Example 2:

	$ python3 l-0169.py --nums 2 2 1 1 1 2 2
	>>> 2
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().majorityElement(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()

if __name__=='__main__':
	main()