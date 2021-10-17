# 167. Two Sum II - Input array is sorted


import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--numbers', nargs='+', type=int, metavar='n, n ,n ...', help='Array of integers')
	parser.add_argument('-t', '--target', nargs=1, type=int, metavar='n', help='Target number')
	parser.add_argument('-d', '--description' ,action='store_true', help='Show description')
	parser.add_argument('-e', '--example',action='store_true', help='Show example')

	return parser 


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        for index, num in enumerate(numbers):
            n = target - num
            
            if n in numbers:
                if numbers.index(n) != index:
                    return sorted([index + 1, numbers.index(n) +1])


def main():
	descr = f'''
{Fore.RED}================================================================{Fore.RESET}
{Fore.GREEN}
	# 167. Two Sum II - Input array is sorted

Given a 1-indexed array of integers numbers that 
is already sorted in non-decreasing order, find 
two numbers such that they add up to a specific 
target number. Let these two numbers be numbers[index1] 
and numbers[index2] where 1 <= first < second <= numbers.length.

Return the indices of the two numbers, index1 and index2, 
as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one 
solution. You may not use the same element twice.
{Fore.RESET}
{Fore.RED}================================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0167.py --numbers 2 7 11 15 --target 9
	>>> [1,2]
{Fore.GREEN}
	Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
{Fore.RESET}
Example 2:
	$ python3 l-0167.py --numbers 2 3 4 --target 6
	>>> [1,3]
{Fore.GREEN}
	Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.
{Fore.RESET}
Example 3:
	$ python3 l-0167.py --numbers -1 0 --target -1
	>>> [1,2]
{Fore.GREEN}
	Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.numbers and args.target:
		result = Solution().twoSum(args.numbers, args.target[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
