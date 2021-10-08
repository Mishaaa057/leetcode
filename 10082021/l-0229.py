# 229. Majority Element II


import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, metavar='n', nargs='+', help='Nums array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def majorityElement(self, nums: list) -> list:
        dct = {}
        
        for el in nums:
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        
        result = []
        
        for key in dct:
            if dct[key] > len(nums) / 3:
                result.append(key)
        
        return result


def main():
	descr = f'''
{Fore.RED}=========================================================={Fore.RESET}
{Fore.GREEN}
	#  229. Majority Element II

Given an integer array of size n, find all elements 
that appear more than ⌊ n/3 ⌋ times.
{Fore.RESET}
{Fore.RED}=========================================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0229.py --nums 3 2 3
	>>> [3]

Example 2:
	$ python3 l-0229.py --nums 1
	>>> [1]

Example 3:
	$ python3 l-0229.py --nums 1 2
	>>> [1,2]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().majorityElement(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()

if __name__=='__main__':
	main()