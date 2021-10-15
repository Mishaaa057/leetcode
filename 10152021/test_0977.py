import pytest
s = __import__('l-0977')

def test_case1():
	assert s.Solution().sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]

def test_case2():
	assert s.Solution().sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]

print(s.Solution().sortedSquares([-4,-1,0,3,10]))