# 2022. Convert 1D Array Into 2D Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-o', '--original', nargs='+', type=int, help='An original 1d number array ')
	parser.add_argument('-m', nargs=1, type=int, metavar='n', help='Number of rows')
	parser.add_argument('-n', nargs=1, type=int, metavar='n', help='Number of columns')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def construct2DArray(self, original: list, m: int, n: int) -> list:
        result = []
        if len(original) == (n * m):
            counter = 0
            row = []
            for el in original:
                if counter < n:
                    row.append(el)
                    counter += 1
                    if counter == n:
                        result.append(row)
                        row = []
                        counter = 0

        return result
	

def main():
	descr = f'''
{Fore.RED}=============================================================={Fore.RESET}
{Fore.GREEN}
	# 2022. Convert 1D Array Into 2D Array

You are given a 0-indexed 1-dimensional (1D) integer array 
original, and two integers, m and n. You are tasked with 
creating a 2-dimensional (2D) array with m rows and n columns 
using all the elements from original.

The elements from indices 0 to n - 1 (inclusive) of original 
should form the first row of the constructed 2D array, 
the elements from indices n to 2 * n - 1 (inclusive) should
form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above 
procedure, or an empty 2D array if it is impossible.
{Fore.RESET}
{Fore.RED}=============================================================={Fore.RESET}
	''' 

	example = f'''
Example 1:
	$ python3 l-2022.py --original 1 2 3 4 -m 2 -n 2
	>>> [[1,2],[3,4]]
{Fore.GREEN}
	Explanation:
	The constructed 2D array should contain 2 rows and 2 columns.
	The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
	The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
{Fore.RESET}
Example 2:
	$ python3 l-2022.py --original 1 2 3 -m 1 -n 3
	>>> [[1,2,3]]
{Fore.GREEN}
	Explanation:
	The constructed 2D array should contain 1 row and 3 columns.
	Put all three elements in original into the first row of the constructed 2D array.
{Fore.RESET}
Example 3:
	$ python3 l-2022.py  --original 1 2 -m 1 -n 1
	>>> []
{Fore.GREEN}
	Explanation:
	There are 2 elements in original.
	It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.
{Fore.RESET}
Example 4:
	$ python3 l-2022.py --original 3 -m 1 -n 2
	>>> []
{Fore.GREEN}
	Explanation:
	There is 1 element in original.
	It is impossible to make 1 element fill all the spots in a 1x2 2D array, so return an empty 2D array.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.original and args.m and args.n:
		result = Solution().construct2DArray(args.original, args.m[0], args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()