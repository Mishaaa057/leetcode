# 2089. Find Target Indices After Sorting Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Integer array')
	parser.add_argument('-t', '--target', type=int, nargs=1, help='Target integer')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def targetIndices(self, nums: list, target: int) -> list:
        sorted_nums = sorted(nums)
        
        result = []
        while target in sorted_nums:
            index = sorted_nums.index(target)
            result.append(index)
            sorted_nums[index] = None
        
        return result


def main():
	descr = f'''
{Fore.RED}================================================================{Fore.RESET}
{Fore.GREEN}
	# 2089. Find Target Indices After Sorting Array

You are given a 0-indexed integer array nums and a target 
element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting 
nums in non-decreasing order. If there are no target indices, 
return an empty list. The returned list must be sorted in 
increasing order.
{Fore.RESET}
{Fore.RED}================================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-2089.py --nums 1 2 5 2 3 --target 2
	>>> [1,2]
{Fore.GREEN}
	Explanation: After sorting, nums is [1,2,2,3,5].
	The indices where nums[i] == 2 are 1 and 2.
{Fore.RESET}
Example 2:
	$ python3 l-2089.py --nums 1 2 5 2 3 --target 3
	>>> [3]
{Fore.GREEN}
	Explanation: After sorting, nums is [1,2,2,3,5].
	The index where nums[i] == 3 is 3.
{Fore.RESET}
Example 3:
	$ python3 l-2089.py --nums 1 2 5 2 3 --target 5
	>>> [4]
{Fore.GREEN}
	Explanation: After sorting, nums is [1,2,2,3,5].
	The index where nums[i] == 5 is 4.
{Fore.RESET}
Example 4:
	$ python3 l-2089.py --nums 1 2 5 2 3 --target 4
	>>> []
{Fore.GREEN}
Explanation: There are no elements in nums with value 4.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums and args.target:
		result = Solution().targetIndices(args.nums, args.target[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()