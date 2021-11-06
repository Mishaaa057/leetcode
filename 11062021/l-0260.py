# 260. Single Number III

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-b','--nums', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def singleNumber(self, nums):
        dct = {}
        
        for el in (nums):
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        
        result_list = []
        for key in dct:
            if dct[key] == 1:
                result_list.append(key)
        
        return result_list


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 260. Single Number III


Given an integer array nums, in which exactly 
two elements appear only once and all the other 
elements appear exactly twice. Find the two elements 
that appear only once. You can return the answer 
in any order.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
 	$ python3 l-0260.py --nums 1 2 1 3 2 5
	>>> [3,5]
{Fore.GREEN}
	Explanation:  [5, 3] is also a valid answer.
{Fore.RESET}
Example 2:
	$ python3 l-0260.py --nums -1 0
	>>> [-1,0]

Example 3:
 	$ python3 l-0260.py --nums 0 1
	>>> [1,0]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().singleNumber(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()	


if __name__=='__main__':
	main()