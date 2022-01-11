# 1022. Sum of Root To Leaf Binary Numbers

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-r', '--root', type=int, nargs="+", help='Root of Binaty Tree')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
    	return f"{self.val}:{self.left},{self.right}"


def insertLevelOrder(arr, root, i, n):     
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
 
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right,
                                     2 * i + 2, n)
    return root

def inOrder(root):
    if root != None:
        inOrder(root.left)
        inOrder(root.right)


def path(root, ways=[], temp=''):
    if root != None:
        if root.left == None and root.right == None:
            ways.append(temp+str(root.val))
        else:
            temp = temp + str(root.val)
            path(root.left, ways ,temp)
            path(root.right, ways ,temp)
        

class Solution:
    def sumRootToLeaf(self, root) -> int:
        ways = []
        path(root, ways)
        
        result = 0
        for el in ways:
            result += (int(el, 2))

        return result


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 1022. Sum of Root To Leaf Binary Numbers

You are given the root of a binary tree where each node has a value
0 or 1. Each root-to-leaf path represents a binary number starting
with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could
represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the
path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits
integer.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''
	
	example = f'''
Example 1:
	$ python3 l-1022.py --root 1 0 1 0 1 0 1
	>>> 22
{Fore.GREEN}
	Explanation:
		(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
{Fore.RESET}
Example 2:
	$ python3 l-1022.py --root 0
	>>> 0
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.root:
		n = len(args.root)
		root = None
		root = insertLevelOrder(args.root, root, 0, n)
		inOrder(root)
		result = Solution().sumRootToLeaf(root)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
