# 1991. Find the Middle Index in Array

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Integer Array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def findMiddleIndex(self, nums: list) -> int:
        for index, el in enumerate(nums):
            if sum(nums[:index+1]) == sum(nums[index:]):
                return index
        return -1


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 1991. Find the Middle Index in Array

Given a 0-indexed integer array nums, find the leftmost middleIndex
(i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... +
nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] +
... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0.
Similarly, if middleIndex == nums.length - 1, the right side sum
is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1
if there is no such index.
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1991.py --nums 2 3 -1 8 4
	>>> 3
{Fore.GREEN}
	Explanation:
		The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
		The sum of the numbers after index 3 is: 4 = 4
{Fore.RESET}
Example 2:
	$ python3 l-1991.py --nums 1 -1 4
	>>> 2
{Fore.GREEN}
	Explanation:
		The sum of the numbers before index 2 is: 1 + -1 = 0
		The sum of the numbers after index 2 is: 0
{Fore.RESET}
Example 3:
	$ python3 l-1991.py --nums 2 5
	>>> -1
{Fore.GREEN}
	Explanation:
		There is no valid middleIndex.
{Fore.RESET}
Example 4:
	$ python3 l-1991.py --nums 1
	>>> 0
{Fore.GREEN}
	Explantion:
		The sum of the numbers before index 0 is: 0
		The sum of the numbers after index 0 is: 0
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().findMiddleIndex(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
