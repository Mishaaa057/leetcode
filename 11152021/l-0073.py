# 73. Set Matrix Zeroes
# Difficulty - [Medium]

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-m', '--matrix', type=str, nargs=1, help='Matrix (plseas input as integer)')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def setZeroes(self, matrix: list) -> list:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Get colums indexes where row[index] = 0
        indexes_with_zeroes = []
        
        for index, line in enumerate(matrix):
            if 0 in line:
                for index2, el in enumerate(line):
                    if el == 0:            
                        indexes_with_zeroes.append(index2)
                        # Rewrite row to zeroes
                        line = [0 for x in range(len(line))]
                        matrix[index] = line

        # Put else zeroes
        for line in matrix:
            for el in indexes_with_zeroes:
                line[el] = 0 

        return matrix


def main():
	r = Fore.RED
	e = Fore.RESET
	y = Fore.YELLOW

	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 73. Set Matrix Zeroes

Given an m x n integer matrix matrix, 
if an element is 0, set its entire 
row and column to 0's, and return the matrix.

You must do it in place.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	''' 

	example = f'''
Example 1:
	[1 1 1]      [1 {y}0{e} 1]
	[1 {r}0{e} 1] ===> [{y}0{e}{r} 0{e}{y} 0{e}]
	[1 1 0]      [1 {y}0{e} 1]

	$ python3 l-0073.py --matrix "[[1,1,1],[1,0,1],[1,1,1]]"
	>>> [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
	[{r}0{e} 1 2 {r}0{e}]      [{r}0{e} {y}0 0{e} {r}0{e}]
	[3 4 5 2] ===> [{y}0{e} 4 5 {y}0{e}]
	[1 3 1 5]      [{y}0{e} 3 1 {y}0{e}]

	$ python3 l-0073.py --matrix "[[0,1,2,0],[3,4,5,2],[1,3,1,5]]"
	>>> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.matrix:
		matrix = eval(args.matrix[0])
		result = Solution().setZeroes(matrix)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
	