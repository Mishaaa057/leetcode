# 2057. Smallest Index With Equal Value

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def smallestEqual(self, nums: list) -> int:
        for index, el in enumerate(nums):
            if index % 10 == el:
                return index
            
        return -1


def main():
	descr = f'''
{Fore.RED}============================================================={Fore.RESET}
{Fore.GREEN}
	# 2057. Smallest Index With Equal Value

Given a 0-indexed integer array nums, return the smallest 
index i of nums such that i mod 10 == nums[i], or -1 if 
such index does not exist.

x mod y denotes the remainder when x is divided by y.
{Fore.RESET}
{Fore.RED}============================================================={Fore.RESET}
	'''
	
	example = f'''
Example 1:
	$ python3 l-2057.py --nums 0 1 2
	>>> 0
{Fore.GREEN}
	Explanation: 
		i=0: 0 mod 10 = 0 == nums[0].
		i=1: 1 mod 10 = 1 == nums[1].
		i=2: 2 mod 10 = 2 == nums[2].
		All indices have i mod 10 == nums[i], so we return the smallest index 0.
{Fore.RESET}
Example 2:
	$ python3 l-2057.py --nums 4 3 2 1
	>>> 2
{Fore.GREEN}
	Explanation: 
		i=0: 0 mod 10 = 0 != nums[0].
		i=1: 1 mod 10 = 1 != nums[1].
		i=2: 2 mod 10 = 2 == nums[2].
		i=3: 3 mod 10 = 3 != nums[3].
		2 is the only index which has i mod 10 == nums[i].
{Fore.RESET}
Example 3:
	$ python3 l-2057.py --nums 1 2 3 4 5 6 7 8 9 0
	>>> -1
{Fore.GREEN}
	Explanation: No index satisfies i mod 10 == nums[i].
{Fore.RESET}
Example 4:
	$ python3 l-2057.py --nums 2 1 3 5 2
	>>> 1
{Fore.GREEN}
	Explanation: 1 is the only index with i mod 10 == nums[i].
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().smallestEqual(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
