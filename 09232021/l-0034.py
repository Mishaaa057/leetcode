# 34. Find First and Last Position of Element in Sorted Array
# Difficulty - [Medium]

from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', type=int, metavar='n',
		nargs='+', help='Integer array')
	parser.add_argument('--target', '-t', type=int,metavar='i',
		nargs=1, help='Target')
	parser.add_argument('--description', '-d', action='store_true',
		help='Show description')
	parser.add_argument('--example', '-e', action='store_true',
		help='Show example')

	return parser 


class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        result = []
        
        # find start
        for index, el in enumerate(nums):
            if el == target:
                result.append(index)
                break
        
        #find end
        index = len(nums) - 1
        while index >= 0:
            if nums[index] == target:
                result.append(index)
                break
            index -= 1
        
        if result != []:
            return result
        else:
            return [-1, -1]


def Main():
	descr = f'''
{Fore.RED}========================================================================{Fore.RESET}
	{Fore.GREEN}# 34. Find First and Last Position of Element 
				in Sorted Array

Given an array of integers nums sorted in ascending order, find the 
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].{Fore.RESET}
{Fore.RED}========================================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0034.py --nums 5 7 7 8 8 10 --target 8
	>>> [3,4]

Example 2:
	$ python3 l-0034.py --nums 5 7 7 8 8 10 --target 6
	>>>[-1,-1]

Example 3:
	$ python3 l-0034.py --nums 0 --target 0
	>>> [0, 0]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums and args.target:
		result = Solution().searchRange(args.nums, args.target[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()
