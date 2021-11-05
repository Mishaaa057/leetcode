# 441. Arranging Coins


import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', type=int, nargs=1, metavar='n', help='Some Integer')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        
        for i in range(1, n + 1):
            if n >= i:
                n -= i
            else:
                return (i - 1)
        

def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 441. Arranging Coins

You have n coins and you want to build a 
staircase with these coins. The staircase 
consists of k rows where the ith row has 
exactly i coins. The last row of the 
staircase may be incomplete.

Given the integer n, return the number of 
complete rows of the staircase you will build.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0441.py -n 5
	>>> 2
{Fore.GREEN}
	Explanation: Because the 3rd row is incomplete, we return 2.
{Fore.RESET}
Example 2:
	$ python3 l-0441.py -n 8
	>>> 3
{Fore.GREEN}
	Explanation: Because the 4th row is incomplete, we return 3.
{Fore.RESET}
	''' 

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.n:
		result = Solution().arrangeCoins(args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()