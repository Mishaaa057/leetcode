#21. Merge Two Sorted Lists

import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-l1', '--list1', nargs='+', type=int, metavar='n', help='Linked List 1')
	parser.add_argument('-l2', '--list2', nargs='+', type=int, metavar='n', help='Linked List 2')
	parser.add_argument('-n', nargs=1, type=int, metavar='n', help='N-th element to remove from the end')
	parser.add_argument('-d', '--description' ,action='store_true', help='Show description')
	parser.add_argument('-e', '--example',action='store_true', help='Show example')

	return parser 


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


# Generate new Node
def new_node(values):
    # Reverse values
    lst = []
    for el in values:
        lst = [el] + lst
        
        # Generate new node list from reversed values 
    x = None
    for el in lst:
        x = ListNode(el, next=x)
    return x


class Solution:
    def mergeTwoLists(self, l1, l2):
        values1 = []
        values2 = []
        get_values(l1, values1)
        get_values(l2, values2)
        
        values = values1 + values2
        values = sorted(values)
        
        return new_node(values)


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	#21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a 
sorted list. The list should be made by splicing
together the nodes of the first two lists.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0021.py --list1 1 2 4 --list2 1 3 4
	>>> [1,1,2,3,4,4]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.list1 and args.list2:
		node1 = new_node(args.list1)
		node2 = new_node(args.list2)

		result_node = Solution().mergeTwoLists(node1, node2)

		print(result_node)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()