# 442. Find All Duplicates in an Array
# Difficulty - [Medium]


from colorama import Fore
import argparse


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def findDuplicates(self, nums: list) -> list:
        dct = {}
        result = []
        
        for index, el in enumerate(nums):
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        
        for key in dct:
            if dct[key] >= 2:
                result.append(key)
        
        return result


def main():
	descr = f'''
{Fore.RED}==============================================================={Fore.RESET}
{Fore.GREEN}
	# 442. Find All Duplicates in an Array

Given an integer array nums of length n where all the 
integers of nums are in the range [1, n] and each integer 
appears once or twice, return an array of all the integers 
that appears twice.

You must write an algorithm that runs in O(n) time and uses 
only constant extra space.
{Fore.RESET}
{Fore.RED}==============================================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0442.py --nums 4 3 2 7 8 2 3 1
	>>> [3, 2]

Example 2:
	$ python3 l-0442.py --nums 1 1 2
	>>> [1]

Example 3:
	$ python3 l-0442.py --nums 1
	>>> []
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().findDuplicates(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
