# 1572. Matrix Diagonal Sum

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-m', '--matrix', type=str, nargs=1, help='Matrix (input as string)')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def diagonalSum(self, mat: list) -> int:
        # count primary diagonal
        counter = 0
        for i in range(len(mat)):
            counter += mat[i][i]
        
        # reverse matrix to count secondary diagonal 
        for index, line in enumerate(mat):
            mat[index] = line[::-1]
        
        counter2 = 0
        for i in range(len(mat)):
            counter2 += mat[i][i]
            
        
        # remove central point
        if len(mat) % 2 != 0:
            i = (len(mat) // 2)
            central = mat[i][i]
            counter2 -= central
        
        # return result
        result = counter + counter2
        return result
	
	
def main():
	descr = f'''
{Fore.RED}====================================================================={Fore.RESET}
{Fore.GREEN}
	# 1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix 
diagonals.

Only include the sum of all the elements on the primary diagonal 
and all the elements on the secondary diagonal that are not part 
of the primary diagonal.
{Fore.RESET}
{Fore.RED}====================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	[1 2 3]
	[4 5 6]
	[7 8 9]

	$ python3 l-1572.py --matrix "[[1,2,3],[4,5,6],[7,8,9]]"
	>>> 25
{Fore.GREEN}
	Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
	Notice that element mat[1][1] = 5 is counted only once.
{Fore.RESET}
Example 2:
	$ python3 l-1572.py --matrix "[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]"
	>>> 8

Example 3:
	$ python3 l-1572.py --matrix "[[5]]"
	>>> 5
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.matrix:
		matrix = eval(args.matrix[0])
		result = Solution().diagonalSum(matrix)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
