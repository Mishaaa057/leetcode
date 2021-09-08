# 1979. Find Greatest Common Divisor of Array

import argparse
from math import gcd


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


class Solution:
    def findGCD(self, nums):
        maximum = max(nums)
        minimum = min(nums)
        return gcd(maximum, minimum)


def Main():
	descr = '''
Given an integer array nums, return the greatest common divisor of
the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive 
integer that evenly divides both numbers.
	'''

	example = '''
Example 1:
	Input: nums = [2,5,6,9,10]
	Output: 2
	Explanation:
	The smallest number in nums is 2.
	The largest number in nums is 10.
	The greatest common divisor of 2 and 10 is 2.

Example 2:
	Input: nums = [7,5,6,8,3]
	Output: 1
	Explanation:
	The smallest number in nums is 3.
	The largest number in nums is 8.
	The greatest common divisor of 3 and 8 is 1.

Example 3:

	Input: nums = [3,3]
	Output: 3
	'''
	

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums != None :
		result = Solution().findGCD(args.nums)
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()

if __name__ == '__main__':
	Main()	