# 203. Remove Linked List Elements

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--head', type=int, nargs='+', help='Head of Linked List')
	parser.add_argument('-val', '--value', type=int, nargs=1, help='Integer to remove')
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
    def removeElements(self, head, val: int):
        # Get values from list node
        values = []
        get_values(head, values)
        
        # Remove val from values
        while val in values:
            values.remove(val)
        
        # Generate new node list and return it
        return new_node(values)
	

def main():
	descr = f'''
{Fore.RED}========================================================{Fore.RESET}
{Fore.GREEN}
	# 203. Remove Linked List Elements

Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has 
Node.val == val, and return the new head.
{Fore.RESET}
{Fore.RED}========================================================{Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0203.py --head 1 2 6 3 4 5 6 -val 6
	>>> [1,2,3,4,5]

Example 2:
	$ python3 l-0203.py --head 7 7 7 7 -val 7
	>>> []
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.head and args.value:
		head = new_node(args.head)
		result_node = Solution().removeElements(head, args.value[0])
		result_values = []
		get_values(result_node, result_values)

		print(result_values)
	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()