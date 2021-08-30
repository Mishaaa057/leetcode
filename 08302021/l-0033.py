import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', type=int, nargs='+', help='List of numbers')
	parser.add_argument('--target', '-t', type=int, nargs=1, help='Target')
	parser.add_argument('-d', nargs='*', help='Show description')
	parser.add_argument('-e', nargs='*', help='Show example')

	return parser


class Solution:
    def search(self, nums, target):
        
        for index, num in enumerate(nums):
            if num == target:
                return index
        return -1


def Main():
	descr = '''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index
k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1],
..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] 
might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.
'''


	example = '''
Example 1:
	Input: nums = [4,5,6,7,0,1,2], target = 0
	Output: 4

Example 2:
	Input: nums = [4,5,6,7,0,1,2], target = 3
	Output: -1

Example 3:
	Input: nums = [1], target = 0
	Output: -1
'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums != None and args.target != None:
		result = Solution().search(args.nums, args.target[0])
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()