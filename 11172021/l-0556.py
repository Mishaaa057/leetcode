# 566. Reshape the Matrix

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-m', '--matrix', type=str, help='Matrix (please, input as string)')
	parser.add_argument('-r', type=int, nargs=1, metavar='N', help='Number of rows')
	parser.add_argument('-c', type=int, nargs=1, metavar='N', help='Number of columns')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def matrixReshape(self, mat: list, r: int, c: int) -> list:
        
        # Get elements form mat
        elements = []
        for line in mat:
            elements += line
        
        # Check if can make new matrix
        if len(elements) == (r * c):
            
            # Generate result matrix
            result = []
            line = []
            counter = 0
            for el in elements:
                
                if counter == c - 1:
                    line.append(el)
                    result.append(line)
                    line = []
                    counter = 0
                else:
                    line.append(el)
                    counter += 1
            
            return result
        return mat


def main():
	descr = f'''
{Fore.RED}=================================================================={Fore.RESET}
{Fore.GREEN}
	# 566. Reshape the Matrix

In MATLAB, there is a handy function called reshape which 
can reshape an m x n matrix into a new one with a different 
size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c 
representing the number of rows and the number of columns 
of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements 
of the original matrix in the same row-traversing order as 
they were.

If the reshape operation with given parameters is possible 
and legal, output the new reshaped matrix; Otherwise, 
output the original matrix.
{Fore.RESET}
{Fore.RED}=================================================================={Fore.RESET}
	'''

	example = '''
Example 1:
	[1 2] 
	[3 4] ===> [1 2 3 4]

	$ python3 l-0556.py --matrix "[[1,2],[3,4]]" -r 1 -c 4
	>>> [[1,2,3,4]]

Example 2:
	[1 2]      [1 2]
	[3 4] ===> [3 4]

	$ python3 l-0556.py --matrix "[[1,2],[3,4]]" -r 2 -c 4
Output: [[1,2],[3,4]]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.matrix and args.r and args.c:
		matrix = eval(args.matrix)
		result = Solution().matrixReshape(matrix, args.r[0], args.c[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()