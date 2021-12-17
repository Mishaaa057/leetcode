# 1122. Relative Sort Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-ar1', '--arrey1', type=str, nargs='+', help='Array 1')
	parser.add_argument('-ar2', '--arrey2', type=str, nargs='+', help='Array 2')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        result = []
        arr1 = sorted(arr1)
        for el in arr2:
            if el in arr1:
                while el in arr1:
                    result.append(el)
                    arr1.remove(el)
        result += arr1
        return result


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
Given two arrays arr1 and arr2, the elements of arr2 are distinct,
and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items
in arr1 are the same as in arr2. Elements that do not appear in arr2
should be placed at the end of arr1 in ascending order.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1122.py --arrey1 2 3 1 3 2 4 6 7 9 2 19 --arrey2 2 1 4 3 9 6
	>>> [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
	$ python3 l-1122.py --arrey1 28 6 22 8 44 17 --arrey2 22 28 8 6
	>>> [22,28,8,6,17,44]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.arrey1 and args.arrey2:
		result = Solution().relativeSortArray(args.arrey1, args.arrey2)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()