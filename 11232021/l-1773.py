# 1773. Count Items Matching a Rule

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--items', type=str, nargs=1, help='Items grid (input as string)')
	parser.add_argument('--rulekey', type=str, nargs=1, help='RuleKey')
	parser.add_argument('--rulevalue', type=str, nargs=1, help='RuleValue')
	parser.add_argument('-d', '--description', action='store_true', help='Show descripotion')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser 


class Solution:
    def countMatches(self, items: list, ruleKey: str, ruleValue: str) -> int:
        
        if ruleKey == 'type':
            i = 0
        elif ruleKey == 'color':
            i = 1
        elif ruleKey == 'name':
            i = 2
            

        counter = 0
        for item in items:
        	
            if item[i] == ruleValue:
            	counter += 1
        
        return counter


def main():
	descr = f'''
{Fore.RED}=================================================================={Fore.RESET}
{Fore.GREEN}
	# 1773. Count Items Matching a Rule

You are given an array items, where each items[i] = [typei, 
colori, namei] describes the type, color, and name of the 
ith item. You are also given a rule represented by two 
strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the 
following is true:

	ruleKey == "type" and ruleValue == typei.
	ruleKey == "color" and ruleValue == colori.
	ruleKey == "name" and ruleValue == namei.
	Return the number of items that match the given rule.
{Fore.RESET}
{Fore.RED}=================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1773.py --items '[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]' --rulekey "color" --rulevalue "silver"
	>>> 1
{Fore.GREEN}
	Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
{Fore.RESET}
Example 2:
	$ python3 l-1773.py --items '[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]' --rulekey "type" --rulevalue "phone"
	>>> 2
{Fore.GREEN}
	Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.items and args.rulekey and args.rulevalue:
		items = eval(args.items[0])
		result = Solution().countMatches(items, args.rulekey[0], args.rulevalue[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()


	