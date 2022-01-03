# 234. Palindrome Linked List

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
    def isPalindrome(self, head: list) -> bool:
        values = []
        get_values(head, values)
        
        return values == values[::-1]


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a
palindrome.
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0234.py --head 1 2 2 1
	>>> True

Example 2:
	$ python3 l-0234.py --head 1 2
	>>> False
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.head:
		node = new_node(args.head)
		result = Solution().isPalindrome(node)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()	


if __name__=='__main__':
	main()
