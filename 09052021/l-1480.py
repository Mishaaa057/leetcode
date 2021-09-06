# Running Sum of 1d Array

import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', nargs='+', type=int, help='Numbers Array')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


class Solution:
    def runningSum(self, nums):
        result_lst = []
        
        for index, num in enumerate(nums):
            number = 0
            for index2, num2 in enumerate(nums):
                if index2 <= index:
                    number += num2
            result_lst.append(number)
        
        
        return result_lst


def Main():
	descr = '''
Given an array nums. We define a running sum 
of an array as runningSum[i] = sum(nums[0]…nums[i]).
	'''

	example = '''
Example 1:
	Input: nums = [1,2,3,4]
	Output: [1,3,6,10]

Example 2:
	Input: nums = [1,1,1,1,1]
	Output: [1,2,3,4,5]

Example 3:
	Input: nums = [3,1,2,10,1]
	Output: [3,4,6,16,17]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()


	if args.nums != None:
		result = Solution().runningSum(args.nums)
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()

if __name__=='__main__':
	Main()
