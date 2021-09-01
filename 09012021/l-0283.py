# Move zeroes

import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


class Solution:
    def moveZeroes(self, nums):
        
        for el in nums:
            if el == 0:
                nums.remove(el)
                nums.append(el)
        return nums


def Main():
	descr = '''
Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
	'''             

	example = '''
Example 1:
	Input: nums = [0,1,0,3,12]
	Output: [1,3,12,0,0]

Example 2:
	Input: nums = [0]
	Output: [0]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums != None:
		result = Solution().moveZeroes(args.nums)
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()

