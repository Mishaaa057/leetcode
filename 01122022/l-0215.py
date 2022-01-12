# 215. Kth Largest Element in an Array

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
    def findKthLargest(self, nums: list, k: int) -> int:
        nums = sorted(nums)[::-1]
        return nums[k-1]
        


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 215. Kth Largest Element in an Array
	
Given an integer array nums and an integer k, return the kth largest
element in the array.

Note that it is the kth largest element in the sorted order, not the
kth distinct element.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0215.py --nums 3 2 1 5 6 4 -k 2
	>>> 5
Example 2:
	$ python3 l-0215.py --nums 3 2 3 1 2 4 5 5 6 -k 4
	>>> 4
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums and args.k:
		result = Solution().findKthLargest(args.nums, args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()