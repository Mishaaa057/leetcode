# 961. N-Repeated Element in Size 2N Array


import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', nargs='+', type=int, metavar='n', help='Integer array')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	parser.add_argument('-d', '--description', action='store_true', help='Description')

	return parser


class Solution:
    def repeatedNTimes(self, nums):
        lst = []
        
        for el in nums:
            if el not in lst:
                lst.append(el)
            else:
                return el


def Main():
	descr ='''
#0961 N-Repeated Element in Size 2N Array

You are given an integer array nums with the following properties:
	nums.length == 2 * n.
	nums contains n + 1 unique elements.
	Exactly one element of nums is repeated n times.
Return the element that is repeated n times.
	'''

	example = '''
Example 1:
	$ python3 --nums 1 2 3 3
	>>> 3

Example 2:
	$ python3 --nums 2 1 2 5 3 2
	>>> 2 

Example 3:
	$ python3 --nums 5 1 5 2 5 3 5 4
	>>> 5
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().repeatedNTimes(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__ == '__main__':
	Main()