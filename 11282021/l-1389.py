# 1389. Create Target Array in the Given Order

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', type=int, nargs='+', help='Integer arrey numbers')
	parser.add_argument('--index', type=int, nargs='+', help='Integer arrey of indexes')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def createTargetArray(self, nums: list, index: list) -> list:
        res = []
        
        for idx, el  in enumerate(nums):
            res = res[:index[idx]] + [el] + res[index[idx]:]
        return res


def main():
	descr = f'''
{Fore.RED}==================================================================={Fore.RESET}
{Fore.GREEN}
	# 1389. Create Target Array in the Given Order

Given two arrays of integers nums and index. Your task is to 
create target array under the following rules:

	[*] Initially target array is empty.

	[*]	From left to right read nums[i] and index[i], insert 
		at index index[i] the value nums[i] in target array.

	[*]	Repeat the previous step until there are no elements 
		to read in nums and index.
		Return the target array.

It is guaranteed that the insertion operations will be valid.
{Fore.RESET}
{Fore.RED}==================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1389.py --nums 0 1 2 3 4 --index 0 1 2 2 1
	>>> [0,4,1,3,2]
{Fore.GREEN}
	Explanation:
	nums       index     target
	0            0        [0]
	1            1        [0,1]
	2            2        [0,1,2]
	3            2        [0,1,3,2]
	4            1        [0,4,1,3,2]
{Fore.RESET}
Example 2:
	$ python3 l-1389.py --nums 1 2 3 4 0 --index 0 1 2 3 0
	>>> [0,1,2,3,4]
{Fore.GREEN}
	Explanation:
	nums       index     target
	1            0        [1]
	2            1        [1,2]
	3            2        [1,2,3]
	4            3        [1,2,3,4]
	0            0        [0,1,2,3,4]
{Fore.RESET}
Example 3:
	$ python3 l-1389.py --nums 1 --index 0
	>>> [1]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums and args.index:
		result = Solution().createTargetArray(args.nums, args.index)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()