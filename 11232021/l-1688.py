# 1688. Count of Matches in Tournament

import argparse 
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', type=int, nargs=1, metavar='N', help='An integer n')
	parser.add_argument('-d', '--description', action='store_true', help='Show descripotion')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1


def main():
	descr = f'''
{Fore.RED}===================================================================={Fore.RESET}
{Fore.GREEN}
	# 1688. Count of Matches in Tournament

You are given an integer n, the number of teams in a tournament 
that has strange rules:

If the current number of teams is even, each team gets 
paired with another team. A total of n / 2 matches are 
played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly 
advances in the tournament, and the rest gets paired. A total 
of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams 
advance to the next round.

Return the number of matches played in the tournament 
until a winner is decided.
{Fore.RESET}
{Fore.RED}===================================================================={Fore.RESET}
	'''
	
	example = f'''
Example 1:
	$ python3 l-1688.py -n 7
	>>> 6
{Fore.GREEN}
	Explanation: Details of the tournament: 
	- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
	- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
	- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
	Total number of matches = 3 + 2 + 1 = 6.
{Fore.RESET}
Example 2:
	$ python3 l-1688.py -n 14
	>>> 13
{Fore.GREEN}
	Explanation: Details of the tournament:
	- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
	- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
	- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
	- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
	Total number of matches = 7 + 3 + 2 + 1 = 13.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.n:
		result = Solution().numberOfMatches(args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
	