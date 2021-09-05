# Build Array from Permutation

import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


class Solution:
    def buildArray(self, nums: list):
        new_lst = []
        
        for index, num in enumerate(nums):
            new_lst.append(nums[nums[index]])
        
        return new_lst

def Main():
	descr = '''
Given a zero-based permutation nums (0-indexed),
build an array ans of the same length where ans[i] = nums[nums[i]] 
for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers 
from 0 to nums.length - 1 (inclusive).
	'''

	example = '''
Example 1:
	Input: nums = [0,2,1,5,3,4]
	Output: [0,1,2,4,5,3]
	Explanation: The array ans is built as follows: 
	ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
	    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    	= [0,1,2,4,5,3]

Example 2:
	Input: nums = [5,0,1,2,3,4]
	Output: [4,5,0,1,2,3]
	Explanation: The array ans is built as follows:
	ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
	    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
	    = [4,5,0,1,2,3]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums != None:
		result = Solution().buildArray(args.nums)
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()

if __name__ == '__main__':
	Main()	