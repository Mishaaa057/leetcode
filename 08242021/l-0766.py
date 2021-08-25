import argparse


descr = '''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
'''


parser = argparse.ArgumentParser(description=descr)
parser.add_argument('-args',   nargs='+')
parser.add_argument('-d', help='Show description', nargs='*')
parser.add_argument('-e', help='Example how to use script', nargs='*')

args = parser.parse_args()


def converte_to_matrix(lst):

	lst1 = lst[1:]
	lst1 = lst1[:-1]
	# '[4, 3], [5]'	
	
	
	matrix = []
	temp_lst = []
	
	for el in lst1:
		if el != '[' and el != ']' and el != ',' and el != ' ':
			temp_lst.append(int(el))
		elif el == ']':
			matrix.append(temp_lst)
			temp_lst = []

	return matrix


class Solution:
    def isToeplitzMatrix(self, matrix):
        
        result = True
        for r, row in enumerate(matrix):
            if r != 0:
                 for n, el in enumerate(row):
                        if n != 0:
                            
                            if matrix[r][n] != matrix[r -1][n-1]:
                                return False
        return result


def Main():

	
	if args.d != None:
		print(descr)

	if args.e != None:
		print('Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]\n'
		'Output: true')
	

	if args.args != None:
		lst_with_args = args.args
		for lst in lst_with_args:
			matrix = converte_to_matrix(lst)
			
			print(Solution().isToeplitzMatrix(matrix))




if __name__=='__main__':
	Main()