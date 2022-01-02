# 2006. Count Number of Pairs With Absolute Difference K

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Integer Array')
	parser.add_argument('-k', type=int, nargs=1, help='Integer K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def countKDifference(self, nums: list, k: int) -> int:
        
        counter = 0
        for index1, el1 in enumerate(nums):
            for index2, el2 in enumerate(nums[:index1+1]):
                if index1 != index2:
                    if abs(el1 - el2) == k:
                        counter += 1
        
        return counter


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 2006. Count Number of Pairs With Absolute Difference K

Given an integer array nums and an integer k, return the number of
pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:
		x if x >= 0.
		-x if x < 0.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-2006.py --nums 1 2 2 1 -k 1
	>>> 4

Example 2:
	$ python3 l-2006.py --nums 1 3 -k 3
	>>> 0

Example 3:
	$ python3 l-2006.py --nums 3 2 1 5 4 -k 2
	>>> 3
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums and args.k:
		result = Solution().countKDifference(args.nums, args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
