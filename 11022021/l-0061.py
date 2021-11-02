# 61. Rotate List
# Difficulty - [Medium]

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--head', type=int, nargs='+', help='Head of Linked list')
	parser.add_argument('-k', type=int, nargs=1, help='Some integer K')
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


class Solution:
    def rotateRight(self, head, k: int):
    	# Get list of values from node list
        values = []
        get_values(head, values)
        
        if values == []:
            return new_node([])
        
        # Check if k < values
        if len(values) < k:
            k = k % len(values)
        
		# Swap last k elements with elements before and generate new list
        new_values = []

       	end = values[-k:]
        start = values[:-k]
        
        new_values += end
        new_values += start
        
        # Generate result Node list
        result_node = new_node(new_values)
        return result_node


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 61. Rotate List

Given the head of a linked list, 
rotate the list to the right by k places.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0061.py --head 1 2 3 4 5 -k 2
	>>> [4,5,1,2,3]

Example 2:
	$ python3 l-0061.py --head 0 1 2 -k 4
	>>> [2,0,1]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.head and args.k:
		node = new_node(args.head)
		result = Solution().rotateRight(node, args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()	


if __name__=='__main__':
	main()
