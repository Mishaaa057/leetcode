# 1051. Height Checker

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--heights', type=int, nargs='+', metavar='n', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser 


class Solution:
    def heightChecker(self, heights: list) -> int:
        excepted = sorted(heights)
        
        counter = 0
        for index, el in enumerate(heights):
            if el != excepted[index]:
                counter += 1
        
        return counter


def main():
	descr = f'''
{Fore.RED}=================================================={Fore.RESET}
{Fore.GREEN}
	# 1051. Height Checker

A school is trying to take an annual photo of all 
the students. The students are asked to stand in 
a single file line in non-decreasing order by 
height. Let this ordering be represented by the 
integer array expected where expected[i] is the 
expected height of the ith student in line.

You are given an integer array heights representing 
the current order that the students are standing in. 
Each heights[i] is the height of the ith student in 
line (0-indexed).

Return the number of indices where heights[i] != expected[i].
{Fore.RESET}
{Fore.RED}=================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1051.py --heights 1 1 4 2 1 3
	>>> 3
{Fore.GREEN}
	Explanation: 
	heights:  [1,1,4,2,1,3]
	expected: [1,1,1,2,3,4]
	Indices 2, 4, and 5 do not match.
{Fore.RESET}
Example 2:
	$ python3 l-1051.py --heights 5 1 2 3 4
	>>> 5
{Fore.GREEN}
	Explanation:
	heights:  [5,1,2,3,4]
	expected: [1,2,3,4,5]
	All indices do not match.
{Fore.RESET}
Example 3:
	$ python3 l-1051.py --heights 1 2 3 4 5
	>>> 0
{Fore.GREEN}
	Explanation:
	heights:  [1,2,3,4,5]
	expected: [1,2,3,4,5]
	All indices match.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.heights:
		result = Solution().heightChecker(args.heights)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
