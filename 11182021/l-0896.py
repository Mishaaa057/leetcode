# 896. Monotonic Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Iteger array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser


class Solution:
    def isMonotonic(self, nums:list) -> bool:
        lst1 = sorted(nums)
        lst2 = lst1[::-1]
        
        return nums == lst1 or nums == lst2


def main():
	descr = f'''
{Fore.RED}================================================================{Fore.RESET}
{Fore.GREEN}
	# 896. Monotonic Array

An array is monotonic if it is either monotone increasing or 
monotone decreasing.

An array nums is monotone increasing if for all i <= j, 
nums[i] <= nums[j]. An array nums is monotone decreasing 
if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given 
array is monotonic, or false otherwise.
{Fore.RESET}
{Fore.RED}================================================================{Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0896.py --nums 1 2 2 3
	>>> True

Example 2:
	$ python3 l-0896.py --nums 6 5 4 4
	>>> True

Example 3:
	$ python3 l-0896.py --nums 1 3 2
	>>> False

Example 4:
	$ python3 l-0896.py --nums 1 2 4 5
	>>> True

Example 5:
	$ python3 l-0896.py --nums 1 1 1
	>>> True
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().isMonotonic(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()