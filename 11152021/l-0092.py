# 92. Reverse Linked List II
# Difficulty - [Medium]

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--head', type=int, nargs='+', help='Head of singly linked list')
	parser.add_argument('-l', '--left', type=int, nargs=1, help='Left position to reverse')
	parser.add_argument('-r', '--right', type=int, nargs=1, help='Right position to reverse')
	parser.add_argument('-d', '--description', action='store_true', help='Show descripotion')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
    	list_values = []
    	get_values(self, list_values)
    	return str(list_values)


# Get values of node list
def get_values(head, values):
    if head is not None:
        values.append(head.val)
        if head.next:
            get_values(head.next, values)


# Generate new Node
def new_node(values, return_reversed=False):
    # Reverse values
    if not return_reversed:
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
    def reverseBetween(self, head, left: int, right: int):
        values = []
        get_values(head, values)
        values[left-1:right] = values[left-1:right][::-1]
        return new_node(values)


def main():
	descr = f'''
{Fore.RED}========================================================{Fore.RESET}
{Fore.GREEN}
	# 92. Reverse Linked List II

Given the head of a singly linked list and two 
integers left and right where left <= right, 
reverse the nodes of the list from position 
left to position right, and return the reversed list.
{Fore.RESET}
{Fore.RED}========================================================{Fore.RESET}
	''' 

	r = Fore.RED
	e = Fore.RESET
	example = f'''
Example 1:
	1 {r}2 3 4{e} 5 ==> 1 {r}4 3 2{e} 5 

	$ python3 l-0092.py --head 1 2 3 4 5 --left 2 --right 4
	>>> [1,4,3,2,5]

Example 2:
	$ python3 l-0092.py --head 5 --left 1 --right 1
	>>> [5]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.head and args.left and args.right:
		node = new_node(args.head)

		result = Solution().reverseBetween(node, args.left[0], args.right[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()