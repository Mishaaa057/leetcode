# 876. Middle of the Linked List


import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--head', nargs='+', type=int, metavar='n', help='Head of Linked List')
	parser.add_argument('-d', '--description' ,action='store_true', help='Show description')
	parser.add_argument('-e', '--example',action='store_true', help='Show example')

	return parser 

# List Node 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Get values of node list
def get_values(head, values):
    values.append(head.val)
    if head.next:
        get_values(head.next, values)


# Generate new Node List
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
    def middleNode(self, head: ListNode) -> ListNode:
        values = []
        get_values(head, values)
        mid_values = values[len(values) // 2:]
        return new_node(mid_values) 


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 876. Middle of the Linked List

Given the head of a singly linked list, 
return the middle node of the linked list.

If there are two middle nodes, return 
the second middle node.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0876.py --head 1 2 3 4 5
	>>> [3,4,5]
{Fore.GREEN}
	Explanation: The middle node of the list is node 3.
{Fore.RESET}
Example 2:
	$ python3 l-0876.py --head 1 2 3 4 5 6
	>>> [4,5,6]
{Fore.GREEN}
	Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.head:
		head = new_node(args.head)
		result = Solution().middleNode(head)

		# Get Values from Linked list
		values = []
		get_values(result, values)
		print(values)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()