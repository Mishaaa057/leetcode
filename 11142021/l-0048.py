# 48. Rotate Image
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
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Get list values of rotated matrix 
        s = []
        for i in range(len(matrix)):
            temp = []
            for line in matrix:
                temp.append(line[i])
            temp = temp[::-1]
            s += (temp)
        
        
        # Modify original matrix
        counter = 0
        for idx1, line in enumerate(matrix):
            for idx2, el in enumerate(matrix):
                matrix[idx1][idx2] = s[counter]
                counter += 1

        return matrix


def main():
	descr = f'''
{Fore.RED}==========================================================={Fore.RESET}
{Fore.GREEN}
	# 48. Rotate Image

You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you
have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.
{Fore.RESET}
{Fore.RED}==========================================================={Fore.RESET}
	'''
	
	example = f'''
Example 1:
	[1 2 3]         [7 4 1]	
	[4 5 6]	  >>>   [8 5 2]
	[7 8 9]			[9 6 3]

	$ python3 l-0048.py --matrix '[[1,2,3],[4,5,6],[7,8,9]]'
	>>> [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
	[5  1  9  11]         [15 13 2 5 ]
	[2  4  8  10]         [14 3  4 1 ]
	[13 3  6  7 ]  	>>>   [12 6  8 9 ]
	[15 14 12 16]         [16 7 10 11]

	$ python3 l-0048.py --matrix '[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]'
	>>> [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
	$ python3 l-0048.py --matrix '[[1]]'
	>>> [[1]]

Example 4:
	[1 2]         [3 1]
	[3 4]   >>>   [4 2]

	$ python3 l-0048.py --matrix '[[1,2],[3,4]]'
	>>> [[3,1],[4,2]]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.matrix:
		matrix = eval(args.matrix[0])
		result = Solution().rotate(matrix)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()