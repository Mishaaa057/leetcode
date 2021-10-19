# 19. Remove Nth Node From End of List

import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--head', nargs='+', type=int, metavar='n', help='Head of Linked List')
	parser.add_argument('-n', nargs=1, type=int, metavar='n', help='N-th element to remove from the end')
	parser.add_argument('-d', '--description' ,action='store_true', help='Show description')
	parser.add_argument('-e', '--example',action='store_true', help='Show example')

	return parser 



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Get values of node list
def get_values(head, values):
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
    def removeNthFromEnd(self, head, n: int):
        values = []
        get_values(head, values)
        index_to_remove = (len(values) - n)
        values.pop(index_to_remove)
        return new_node(values)


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node 
from the end of the list and return its head.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0019.py --head 1 2 3 4 5 -n 2
	>>> [1,2,3,5]

Example 2:
	$ python3 l-0019.py --head 1 2 -n 1
	>>> [1]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.head and args.n:
		node = new_node(args.head)
		result_node = Solution().removeNthFromEnd(node, args.n[0])
		result = []
		get_values(result_node, result)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()