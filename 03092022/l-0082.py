# 82. Remove Duplicates from Sorted List II


import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--head', type=int, nargs='+', help='Head of Linked list')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
    	values = []
    	get_values(self, values)
    	return str(values)


# Get values of node list
def get_values(head, values):
    if head is not None:
        values.append(head.val)
        if head.next:
            get_values(head.next, values)


# Generate new Reverse Node
def new_node(values, is_not_reverse=True):
    # Reverse values
    if is_not_reverse:
	    lst = []
	    for el in values:
	        lst = [el] + lst
	    values = lst

    # Generate new node list 
    x = None
    for el in values:
        x = ListNode(el, next=x)
    return x


class Solution:
    def deleteDuplicates(self, head):
        values = []
        get_values(head, values)
        
        new_values = []
        for el in values:
            if values.count(el) == 1:
                new_values.append(el)
        
        return new_node(new_values)
        


def main():
	descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate
numbers, leaving only distinct numbers from the original list. Return the
linked list sorted as well.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
    $ python3 l-0082.py --head 1 2 3 3 4 4 5
    >>> [1,2,5]

Example 2:
    $ python3 l-0082.py --head 1 1 1 2 3
    >>> [2,3]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.head:
		node1 = new_node(args.head, is_not_reverse=True)
		result = Solution().deleteDuplicates(node1)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()	


if __name__=='__main__':
	main()