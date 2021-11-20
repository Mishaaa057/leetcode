# 1351. Count Negative Numbers in a Sorted Matrix

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-g', '--grid', type=str, nargs=1, help='Grid (Input as string)')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def countNegatives(self, grid: list) -> int:
        counter = 0
        for line in grid:
            for el in line:
                if el < 0:
                    counter += 1
        
        return counter



def main():
	descr = f'''
{Fore.RED}============================================================={Fore.RESET}
{Fore.GREEN}
	# 1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing 
order both row-wise and column-wise, return the number of 
negative numbers in grid.
{Fore.RESET}
{Fore.RED}============================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1351.py --grid "[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]"
	>>> 8
{Fore.GREEN}
	Explanation: There are 8 negatives number in the matrix.
{Fore.RESET}
Example 2:
	$ python3 l-1351.py --grid "[[3,2],[1,0]]"
	>>> 0

Example 3:
	$ python3 l-1351.py --grid "[[1,-1],[-1,-1]]"
	>>> 3

Example 4:
	$ python3 l-1351.py --grid "[[-1]]"
	>>> 1
	'''
	
	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.grid:
		grid = eval(args.grid[0])
		result = Solution().countNegatives(grid)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()

	