# 1380. Lucky Numbers in a Matrix

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--matrix', type=str, nargs=1, help='Matrix grid (input as string)')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def luckyNumbers(self, matrix: list) -> list:
        lst = []
        
        for index, el in enumerate(matrix[0]):
            temp = []
            for i in range(len(matrix)):
                temp.append(matrix[i][index])
            lst.append(temp)
        
        min_nums = []
        for row in matrix:
            min_nums.append(min(row))
        
        result = []
        for row in lst:
            num = max(row)
            if num in min_nums:
                result.append(num)
        
        return result
        

def main():
	descr = f'''
{Fore.RED}================================================================{Fore.RESET}
{Fore.GREEN}
Given an m x n matrix of distinct numbers, return all lucky 
numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is 
the minimum element in its row and maximum in its column. 
{Fore.RESET}
{Fore.RED}================================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1380.py --matrix "[[3,7,8],[9,11,13],[15,16,17]]"
	>>> [15]
{Fore.GREEN}
	Explanation: 15 is the only lucky number since 
	it is the minimum in its row and the maximum in its column
{Fore.RESET}
Example 2:
	$ python3 l-1380.py --matrix "[[1,10,4,2],[9,3,8,7],[15,16,17,12]]"
	>>> [12]
{Fore.GREEN}
	Explanation: 12 is the only lucky number since 
	it is the minimum in its row and the maximum in its column.
{Fore.RESET}
Example 3:
	$ python3 l-1380.py --matrix "[[7,8],[1,2]]"
	>>> [7]
{Fore.GREEN}
	Explanation: 7 is the only lucky number since 
	it is the minimum in its row and the maximum in its column.
{Fore.RESET}
Example 4:
	$ python3 l-1380.py --matrix "[[3,6],[7,1],[5,2],[4,8]]"
	>>> []
{Fore.GREEN}
	Explanation: There is no lucky number.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.matrix:
		matrix = eval(args.matrix[0])
		result = Solution().luckyNumbers(matrix)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
	
	