# 2133. Check if Every Row and Column Contains All Numbers

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--matrix', type=str, nargs=1, help='Items grid (input as string)')
	parser.add_argument('-d', '--description', action='store_true', help='Show descripotion')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser 


class Solution:
    def checkValid(self, matrix: list) -> bool:
        n = len(matrix)
        arr = list(range(1, n+1))
        

        # check rows
        for row in matrix:
            if sorted(row) != arr:
                return False
        
        # check columns
        for idx in range(n):
            temp = []
            
            for row in matrix:
                temp.append(row[idx])
            
            if sorted(temp) != arr:
                return False
        
        return True


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2133. Check if Every Row and Column Contains All Numbers

An n x n matrix is valid if every row and every column contains all
the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is
valid. Otherwise, return false.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
    $ python3 l-2133.py --matrix "[[1,2,3],[3,1,2],[2,3,1]]"
    >>> True
{Fore.GREEN}
    Explanation:
        In this case, n = 3, and every row and column contains
        the numbers 1, 2, and 3.
        Hence, we return true.
{Fore.RESET}
Example 2:
    $ python3 l-2133.py --matrix "[[1,1,1],[1,2,3],[1,2,3]]"
    >>> False
{Fore.GREEN}
    Explanation:
        In this case, n = 3, but the first row and the first
        column do not contain the numbers 2 or 3.
        Hence, we return false.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.matrix:
		matrix = eval(args.matrix[0])
		result = Solution().checkValid(matrix)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
