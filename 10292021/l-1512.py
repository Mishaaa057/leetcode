# 1512. Number of Good Pairs


import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', metavar='n', help='Integer Array')
	parser.add_argument('-k', type=int, nargs=1, metavar='n', help='K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def numIdenticalPairs(self, nums):
        result = 0
        
        for index1 , el1 in enumerate(nums):
            for index2, el2 in enumerate(nums):
                if index2 > index1:
                    if nums[index1] == nums[index2]:
                        result += 1
        
        return result


def main():
	descr = f'''
{Fore.RED}=================================={Fore.RESET}
{Fore.GREEN}
	# 1512. Number of Good Pairs

Given an array of integers nums, 
return the number of good pairs.

A pair (i, j) is called good if 
nums[i] == nums[j] and i < j.
{Fore.RESET}
{Fore.RED}=================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1512.py --nums 1 2 3 1 1 3
	>>> 4
{Fore.GREEN}
	Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
{Fore.RESET}
Example 2:
	$ python3 l-1512.py --nums  1 1 1 1
	>>> 6
{Fore.GREEN}
	Explanation: Each pair in the array are good.
{Fore.RESET}
Example 3:
	$ python3 l-1512.py --nums  1 2 3
	>>> 0
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().numIdenticalPairs(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()