import pytest
from l0026 import *
def test_case1():
	assert Solution().removeDuplicates([1,1,2])
	print('test1')

def test_case2():
	assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])

def test_case3():
	assert Solution().removeDuplicates([1,1,2,3,3,4,4,4,4,5,5])

test_case1()