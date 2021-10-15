# 977. Squares of a Sorted Array


import argparse
import pytest
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', metavar='n n ...', nargs='+', type=int,help='Integer array nums')
	parser.add_argument('-d', '--description', action='store_true', help='Show description') 
	parser.add_argument('-e', '--example', action='store_true', help='Show example') 
	
	return parser


class Solution:
    def sortedSquares(self, nums: list) -> list:
        result = [n ** 2 for n in nums]
        return sorted(result)


def main():
	descr = f'''
{Fore.RED}============================================================{Fore.RESET}
{Fore.GREEN}
	# 977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in 
non-decreasing order.
{Fore.RESET}
{Fore.RED}============================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0977.py --nums -4 -1 0 3 10
	>>> [0,1,9,16,100]
{Fore.GREEN}	
	Explanation: After squaring, the array becomes [16,1,0,9,100].
	After sorting, it becomes [0,1,9,16,100].
{Fore.RESET}
Example 2:
	$ python3 l-0977.py --nums -7 -3 2 3 11 
	>>> [4,9,9,49,121]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().sortedSquares(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()


def test_case1():
	assert Solution().sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]

def test_case2():
	assert Solution().sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]