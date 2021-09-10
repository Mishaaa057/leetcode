# 1089. Duplicate Zeros


import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--arr', nargs='+', type=int, help='Integer Array')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


class Solution:
    def duplicateZeros(self, arr):
        lst = []        
        for index, el in enumerate(arr):
            if el == 0:
                lst.append(0)
                lst.append(0)
            else:
                lst.append(el)

        for index, el in enumerate(arr):
            arr[index] = lst[index]

        return arr
                      

def Main():
	descr = '''
Given a fixed-length integer array arr, 
duplicate each occurrence of zero, shifting the
remaining elements to the right.

Note that elements beyond the length of the 
original array are not written. Do the above 
modifications to the input array in place and do not 
return anything.


	'''

	example = '''
Example 1:
	Input: arr = [1,0,2,3,0,4,5,0]
	Output: [1,0,0,2,3,0,0,4]
	Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
	Input: arr = [1,2,3]
	Output: [1,2,3]
	Explanation: After calling your function, the input array is modified to: [1,2,3]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()


	if args.arr != None:
		result = Solution().duplicateZeros(args.arr)
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()

if __name__=='__main__':
	Main()
