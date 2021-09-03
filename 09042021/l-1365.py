# How Many Numbers Are Smaller Than the Current Number

import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        lst = []
        for num1 in nums:
            i = 0
            for num2 in nums:
                 if num1 > num2:
                        i += 1
            lst.append(i)
        return lst

def Main():

	descr = '''
Given the array nums, for each nums[i] find out how many numbers in
the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's
such that j != i and nums[j] < nums[i].
	'''             

	example = '''
Example 1:
	Input: nums = [8,1,2,2,3]
	Output: [4,0,1,1,3]

Example 2:
	Input: nums = [6,5,4,8]
	Output: [2,1,0,3]

Example 3:
	Input: nums = [7,7,7,7]
	Output: [0,0,0,0]
	'''
	
	parser = BuildArgParser(descr)
	args = parser.parse_args()
	
	if args.nums != None:
		result = Solution().smallerNumbersThanCurrent(args.nums)
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()