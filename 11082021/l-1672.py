# 1672. Richest Customer Wealth

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--accounts', type=str, nargs=1, help='m x n integer grid accounts (Please, enter as string)')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth_list = []
        for acc in accounts:
            wealth_list.append(sum(acc))
        
        return max(wealth_list)


def main():
	descr = f'''
{Fore.RED}========================================================{Fore.RESET}
{Fore.GREEN}
You are given an m x n integer grid accounts where 
accounts[i][j] is the amount of money the i`th customer 
has in the j`th bank. Return the wealth that the 
richest customer has.

A customer's wealth is the amount of money they 
have in all their bank accounts. The richest 
customer is the customer that has the maximum wealth.
{Fore.RESET}
{Fore.RED}========================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1672.py --accounts '[[1,2,3],[3,2,1]]'
	>>> 6
{Fore.GREEN}
	Explanation:
	1st customer has wealth = 1 + 2 + 3 = 6
	2nd customer has wealth = 3 + 2 + 1 = 6
	Both customers are considered the richest with a wealth of 6 each, so return 6.
{Fore.RESET}
Example 2:
	$ python3 l-1672.py --accounts '[[1,5],[7,3],[3,5]]'
	>>> 10
{Fore.GREEN}
	Explanation: 
	1st customer has wealth = 6
	2nd customer has wealth = 10 
	3rd customer has wealth = 8
	The 2nd customer is the richest with a wealth of 10.
{Fore.RESET}
Example 3:
	$ python3 l-1672.py --accounts '[[2,8,7],[7,1,3],[1,9,5]]'
	>>> 17
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.accounts:
		# Get accounts list from string type argument 
		accounts = eval(args.accounts[0])
		
		result = Solution().maximumWealth(accounts)
		print(result)


	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()