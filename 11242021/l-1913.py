# 1913. Maximum Product Difference Between Two Pairs

import argparse 
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser 


class Solution:
    def maxProductDifference(self, nums: list) -> int:
        c = min(nums)
        nums.remove(c)
        
        d = min(nums)
        
        a = max(nums)
        nums.remove(a)
        
        b = max(nums)
        
        return (a*b)-(c*d)
        

def main():
	descr = f'''
{Fore.RED}================================================================{Fore.RESET}
{Fore.GREEN}
	# 1913. Maximum Product Difference Between Two Pairs

The product difference between two pairs (a, b) and (c, d) 
is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and 
(2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, 
x, y, and z such that the product difference between pairs 
(nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.
{Fore.RESET}
{Fore.RED}================================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1913.py --nums 5 6 2 7 4
	>>> 34
{Fore.GREEN}
	Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
	The product difference is (6 * 7) - (2 * 4) = 34.
{Fore.RESET}
Example 2:
	$ python3 l-1913.py --nums 4 2 5 9 7 4 8
	>>> 64
{Fore.GREEN}
	Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
	The product difference is (9 * 8) - (2 * 4) = 64.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().maxProductDifference(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()