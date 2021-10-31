# 2. Add Two Numbers
# Difficulty - [Medium]


import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--head1', type=int, nargs='+', help='Head of Linked list 1')
	parser.add_argument('--head2', type=int, nargs='+', help='Head of Linked list 2')
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
    def addTwoNumbers(self, l1, l2):
        # Get values from nodes
        values1 = []
        values2 = []
        get_values(l1, values1)
        get_values(l2, values2)
        
        # Reverse values to get correct numbers
        values1 = values1[::-1]
        values2 = values2[::-1]
       
       	# Generate Numbers 
        number1 = ''
        number2 = ''
        
        for el in values1:
            number1 += str(el)
        
        for el in values2:
            number2 += str(el)
        
        number1 = int(number1)
        number2 = int(number2)
        
        # Generate result list from number 1 and 2
        result_number = number1 + number2
        result_list = []
        
        for el in str(result_number):
            result_list.append(int(el))
        
        # Generate result Node from result list
        result_node = new_node(result_list, False)
        
        return result_node


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 2. Add Two Numbers

You are given two non-empty linked lists 
representing two non-negative integers. 
The digits are stored in reverse order, and 
each of their nodes contains a single digit. 
Add the two numbers and return the sum as a 
linked list.

You may assume the two numbers do not contain 
any leading zero, except the number 0 itself.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0002.py --head1 2 4 3 --head2 5 6 4
	>>> [7,0,8]
{Fore.GREEN}
	Explanation: 342 + 465 = 807.
{Fore.RESET}
Example 2:

	$ python3 l-0002.py --head1 0 --head2 0
	>>> [0]

Example 3:
	$ python3 l-0002.py --head1 9 9 9 9 9 9 9 --head2 9 9 9 9
	>>> [8,9,9,9,0,0,0,1]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.head1 and args.head2:
		node1 = new_node(args.head1, is_not_reverse=True)
		node2 = new_node(args.head2, is_not_reverse=True)
		result = Solution().addTwoNumbers(node1, node2)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()	


if __name__=='__main__':
	main()
        
    