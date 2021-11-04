# 23. Merge k Sorted Lists

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--lists', type=str, nargs=1, help='Array of k linked lists (Please, enter as string)')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


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


def get_list(string):
    localsParameter = {'string': string}
    
    lst = eval(string, localsParameter)
    return (lst)


class Solution:
    def mergeKLists(self, lists):
        values = []
        
        # Get Values from all nodes
        for node in lists:
            get_values(node, values)
        
        # Sort all values
        values = sorted(values)
        
        # Generate result Node
        node = new_node(values)
        return node


def main():
	descr = f'''
{Fore.RED}=================================================={Fore.RESET}
{Fore.GREEN}
	# 23. Merge k Sorted Lists

You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted 
linked-list and return it.
{Fore.RESET}
{Fore.RED}=================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0023.py --lists '[[1,4,5],[1,3,4],[2,6]]'
	>>> [1,1,2,3,4,4,5,6]
{Fore.GREEN}
	Explanation: The linked-lists are:
	[
	  1->4->5,
	  1->3->4,
	  2->6
	]
	merging them into one sorted list:
	1->1->2->3->4->4->5->6
{Fore.RESET}
Example 2:
	$ python3 l-0023.py --lists '[]'
	>>> []

Example 3:
	$ python3 l-0023.py --lists '[[]]'
	>>> []
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.lists:
		# Get values from argument
		values = get_list(args.lists[0])
		
		# Generate nodes from values
		nodes = []
		for value in values:
			node = new_node(value)
			nodes.append(node)

		# Get and show result Node
		result = Solution().mergeKLists(nodes)
		if result == None:
			print('[]')
		else:
			print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()