# 88. Merge Sorted Arrayw


import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n1', '--nums1', type=int, nargs='+', metavar='n', help='Integer Array 1')
	parser.add_argument('-n2', '--nums2', type=int, nargs='+', metavar='n', help='Integer Array 2')
	parser.add_argument('-m', type=int, nargs=1, metavar='m', help='Integer M')
	parser.add_argument('-n', type=int, nargs=1, metavar='n', help='Integer N')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_list = []
        
        new_list += nums1[:m]
        new_list += nums2[:n]
        
        new_list = sorted(new_list)
        
        for index, el in enumerate(new_list):
            nums1[index] = el

        return nums1


def main():
	descr = f'''
{Fore.RED}====================================================={Fore.RESET}
{Fore.GREEN}
	# 88. Merge Sorted Arrayw

You are given two integer arrays nums1 and nums2, 
sorted in non-decreasing order, and two integers 
m and n, representing the number of elements in 
nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted 
in non-decreasing order.

The final sorted array should not be returned by 
the function, but instead be stored inside the 
array nums1. To accommodate this, nums1 has a 
length of m + n, where the first m elements denote 
the elements that should be merged, and the last 
n elements are set to 0 and should be ignored. 
nums2 has a length of n.
{Fore.RESET}
{Fore.RED}====================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0088.py --nums1 1 2 3 0 0 0 -m 3 --nums2 2 5 6  -n 3
	>>> [1,2,2,3,5,6]
{Fore.GREEN}	
	Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
	The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
{Fore.RESET}
Example 2:
	$ python3 l-0088.py --nums1 0 -m 0 --nums2 1 -n 1
	>>> [1]
{Fore.GREEN}
	Explanation: The arrays we are merging are [] and [1].
	The result of the merge is [1].
	Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums1 and args.nums2 and args.m and args.n:
		result = Solution().merge(args.nums1, args.m[0], args.nums2, args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
