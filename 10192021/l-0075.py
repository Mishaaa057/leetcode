# 75. Sort Colors
# Difficulty - [Medium]

import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', nargs='+', type=int, metavar='n', help='Array nums')
	parser.add_argument('-d', '--description' ,action='store_true', help='Show description')
	parser.add_argument('-e', '--example',action='store_true', help='Show example')

	return parser


def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        BubbleSort(nums)

        

def main():
	descr = f'''
{Fore.RED}============================================================{Fore.RESET}
{Fore.GREEN}
	# 75. Sort Colors

Given an array nums with n objects colored red, white, 
or blue, sort them in-place so that objects of the 
same color are adjacent, with the colors in the order 
red, white, and blue.

We will use the integers 0, 1, and 2 to represent the 
color red, white, and blue, respectively.

You must solve this problem without using the library's 
sort function.
{Fore.RESET}
{Fore.RED}============================================================{Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0075.py --nums 2 0 2 1 1 0
	>>> [0,0,1,1,2,2]

Example 2:
	$ python3 l-0075.py --nums 2 0 1
	>>> [0,1,2]

Example 3:
	$ python3 l-0075.py --nums 0
	>>> [0]

Example 4:
	$ python3 l-0075.py --nums 1
	>>> [1]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		Solution().sortColors(args.nums)
		print(args.nums)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main() 