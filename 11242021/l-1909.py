# 1909. Remove One Element to Make the Array Strictly Increasing

import argparse 
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser 


class Solution:
    def canBeIncreasing(self, nums: list) -> bool:
        for index, el in enumerate(nums):
            temp = nums.copy()
            temp.pop(index)
            
            l_set = set(temp)
            contains_duplicates = len(l_set) != len(temp)
            
            if temp == sorted(temp) and not contains_duplicates:
                return True
        
        return False
                

def main():
	descr = f'''
{Fore.RED}==================================================================={Fore.RESET}
{Fore.GREEN}
	# 1909. Remove One Element to Make the Array Strictly Increasing

Given a 0-indexed integer array nums, return true if it can be 
made strictly increasing after removing exactly one element, or 
false otherwise. If the array is already strictly increasing, 
return true.

The array nums is strictly increasing if nums[i - 1] < 
nums[i] for each index (1 <= i < nums.length).
{Fore.RESET}
{Fore.RED}==================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1909.py --nums 1 2 10 5 7
	>>> True
{Fore.GREEN}
	Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
	[1,2,5,7] is strictly increasing, so return true.
{Fore.RESET}
Example 2:
	$ python3 l-1909.py --nums 2 3 1 2
	>>> False
{Fore.GREEN}
	Explanation:
	[3,1,2] is the result of removing the element at index 0.
	[2,1,2] is the result of removing the element at index 1.
	[2,3,2] is the result of removing the element at index 2.
	[2,3,1] is the result of removing the element at index 3.
	No resulting array is strictly increasing, so return false.
{Fore.RESET}
Example 3:
	$ python3 l-1909.py --nums 1 1 1
	>>> False
{Fore.GREEN}
	Explanation: The result of removing any element is [1,1].
	[1,1] is not strictly increasing, so return false.
{Fore.RESET}
Example 4:
	$ python3 l-1909.py --nums 1 2 3
	>>> True
{Fore.GREEN}
	Explanation: [1,2,3] is already strictly increasing, so return true.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().canBeIncreasing(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
