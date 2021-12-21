# 860. Lemonade Change

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-b', '--bills', type=int, nargs='+', help='Bills Array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def lemonadeChange(self, bills: list) -> bool:
        lst = []
        for bill in bills:
            if bill == 5:
                lst.append(bill)
                lst = sorted(lst)
            
            elif bill == 10:
                if 5 in lst:
                    lst.append(bill)
                    lst.remove(5)
                    lst = sorted(lst)
                else:
                    return False
            
            else:
                if 5 in lst and 10 in lst:
                    lst.append(20)
                    lst.remove(10)
                    lst.remove(5)
                    lst = sorted(lst)
                elif sum(lst[:3]) == 15:
                    lst = lst[3:]
                    lst.append(20)
                    lst = sorted(lst)
                else:
                    return False
        return True


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 860. Lemonade Change

At a lemonade stand, each lemonade costs $5. Customers are standing
in a queue to buy from you, and order one at a time (in the order
specified by bills). Each customer will only buy one lemonade and pay
with either a $5, $10, or $20 bill. You must provide the correct
change to each customer so that the net transaction is that the
customer pays $5.

Note that you don't have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith
customer pays, return true if you can provide every customer with
correct change, or false otherwise.
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0860.py --bills 5 5 5 10 20
	>>> True
{Fore.GREEN}
	Explanation: 
		From the first 3 customers, we collect three $5 bills in order.
		From the fourth customer, we collect a $10 bill and give back a $5.
		From the fifth customer, we give a $10 bill and a $5 bill.
		Since all customers got correct change, we output true.
{Fore.RESET}
Example 2:
	$ python3 l-0860.py --bills 5 5 10 10 20
	>>> False
{Fore.GREEN}	
	Explanation: 
		From the first two customers in order, we collect two $5 bills.
		For the next two customers in , we collect a $10 bill and give back a $5 bill.
		For the last customer, we can not give change of $15 back because we only have two $10 bills.
		Since not every customer received correct change, the answer is false.
{Fore.RESET}
Example 3:
	$ python3 l-0860.py --bills 5 5 10
	>>> True

Example 4:
	$ python3 l-0860.py --bills 10 10
	>>> False
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.bills:
		result = Solution().lemonadeChange(args.bills)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()