# Search Insert Position

import argparse

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', type=int, nargs='+', help='Sorted number array')
	parser.add_argument('--target', '-t', type=int, nargs=1, help='Target')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


def seacrh_(nums, target):
    for index, el in enumerate(nums):
        if el == target:
            return index

class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            result = seacrh_(nums, target)
            return result
        nums.append(target)
        
        
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1] :
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        return (seacrh_(nums, target))
        
        

def Main():
	descr = '''
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
	'''

	example = '''
Example 1:
	Input: nums = [1,3,5,6], target = 5
	Output: 2

Example 2:
	Input: nums = [1,3,5,6], target = 2
	Output: 1

Example 3:
	Input: nums = [1,3,5,6], target = 7
	Output: 4

Example 4:
	Input: nums = [1,3,5,6], target = 0
	Output: 0

Example 5:
	Input: nums = [1], target = 0
	Output: 0
	'''
	
	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums != None and args.target != None:
		result = Solution().searchInsert(args.nums, args.target[0])
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()
	