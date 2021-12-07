# 1582. Special Positions in a Binary Matrix

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--mat', type=str, nargs=1, help='Matrix (input as string)')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def numSpecial(self, mat: list) -> int:
        counter = 0
        
        indexes_col = []
        for index, el in enumerate(mat[0]):
            n = 0
            for i in range(len(mat)):
                if mat[i][index] == 1:
                    n += 1
            if n == 1:
                indexes_col.append(index)
        
        for line in mat:
            n = 0
            idx = None
            for index, el in enumerate(line):
                if el == 1:
                    idx = index
                    n += 1
            
            if n == 1 and idx in indexes_col:
                counter += 1
    
        return counter


def main():
	descr = f'''
{Fore.RED}=============================================================={Fore.RESET}
{Fore.GREEN}
	# 1582. Special Positions in a Binary Matrix

Given a rows x cols matrix mat, where mat[i][j] is either 
0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and 
all other elements in row i and column j are 0 (rows and 
columns are 0-indexed).
{Fore.RESET}
{Fore.RED}=============================================================={Fore.RESET}
	'''
	
	example = f'''
Example 1:
	$ python3 l-1582.py --mat "[[1,0,0],[0,0,1],[1,0,0]]"
	>>> 1
{Fore.GREEN}
	Explanation: (1,2) is a special position because 
	mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
{Fore.RESET}
Example 2:
	$ python3 l-1582.py --mat "[[1,0,0],[0,1,0],[0,0,1]]"
	>>> 3
{Fore.GREEN}
	Explanation: (0,0), (1,1) and (2,2) are special positions. 
{Fore.RESET}
Example 3:
	$ python3 l-1582.py --mat "[[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]"
	>>> 2
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.mat:
		mat = eval(args.mat[0])
		result = Solution().numSpecial(mat)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()