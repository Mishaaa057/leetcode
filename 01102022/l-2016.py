# 2016. Maximum Difference Between Increasing Elements

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def maximumDifference(self, nums: list) -> int:
        results = []
        for index, el in enumerate(nums):
            for el2 in (nums[index+1:]):
                if el < el2:
                    results.append(el2 - el)
        
        if len(results) > 0:
            return max(results)
        else:
            return -1

def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 2016. Maximum Difference Between Increasing Elements

Given a 0-indexed integer array nums of size n, find the maximum
difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]),
such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-2016.py --nums 7 1 5 4
	>>> 4
{Fore.GREEN}
	Explanation:
		The maximum difference occurs with i = 1 and j = 2,
			nums[j] - nums[i] = 5 - 1 = 4.
		Note that with i = 1 and j = 0, the difference nums[j] 
			- nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
{Fore.RESET}
Example 2:
	$ python3 l-2016.py --nums 9 4 3 2
	>>> -1
{Fore.GREEN}
	Explanation:
		There is no i and j such that i < j and nums[i] < nums[j].
{Fore.RESET}
Example 3:
	$ python3 l-2016.py --nums 1 5 2 10
	>>> 9
{Fore.GREEN}
	Explanation:
		The maximum difference occurs with i = 0 and j = 3,
		nums[j] - nums[i] = 10 - 1 = 9.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().maximumDifference(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
