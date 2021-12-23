# 2099. Find Subsequence of Length K With the Largest Sum


import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Integer Array')
	parser.add_argument('-k', type=int, nargs=1, help='An Integer k')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def maxSubsequence(self, nums: list, k: int) -> list:
        lst = []
        nums2 = nums.copy()
        
        for i in range(k):
            el = max(nums2)
            nums2.remove(el)
            lst.append(el)
        
        sub = []
        for el in nums:
            if el in lst:
                lst.remove(el)
                sub.append(el)
        return sub


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 2099. Find Subsequence of Length K With the Largest Sum

You are given an integer array nums and an integer k. You want to
find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array
by deleting some or no elements without changing the order of the
remaining elements.


{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-2099.py --nums 2 1 3 3 -k 2
	>>> [3,3]
{Fore.GREEN}
	Explanation:
		The subsequence has the largest sum of 3 + 3 = 6.
{Fore.RESET}
Example 2:
	$ python3 l-2099.py --nums -1 -2 3 4 -k 3
	>>> [-1,3,4]
{Fore.GREEN}
	Explanation: 
		The subsequence has the largest sum of -1 + 3 + 4 = 6.
{Fore.RESET}
Example 3:
	$ python3 l-2099.py --nums 3 4 3 3 -k 2
	>>> [3,4]
{Fore.GREEN}
	Explanation:
	The subsequence has the largest sum of 3 + 4 = 7. 
	Another possible subsequence is [4, 3].
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums and args.k:
		result = Solution().maxSubsequence(args.nums, args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
