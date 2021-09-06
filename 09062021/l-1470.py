# 1470. Shuffle the Array

import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', type=int, nargs='+', help='Integer array')
	parser.add_argument('-n', type=int, nargs=1, help='n')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


class Solution:
    def shuffle(self, nums, n):
        n1 = []
        n2 = []
        
        for index, num in enumerate(nums):
            if index < len(nums) / 2:
                n1.append(num)
            else:
                n2.append(num)
        
        result = []
        for index, num in enumerate(n1):
            result.append(num)
            try:
                result.append(n2[index])
            except:
                pass
        return result

def Main():
	descr ='''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
	'''

	example = '''
Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
	'''
	

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums != None and args.n != None:
		result = Solution().shuffle(args.nums, args.n[0])
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()

if __name__ == '__main__':
	Main()	