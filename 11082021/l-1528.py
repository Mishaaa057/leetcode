# 1528. Shuffle String

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', type=str, nargs=1, help='String')
	parser.add_argument('-i', '--indices', type=int, nargs='+', metavar='n', help='Indices')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def restoreString(self, s: str, indices) -> str:
        result_string = '' 
        for i in range(len(s)):
            ind = (indices.index(i))
            result_string += s[ind]
        
        return result_string


def main():
	descr = f'''
{Fore.RED}=================================================={Fore.RESET}
{Fore.GREEN}
	# 1528. Shuffle String

Given a string s and an integer array indices 
of the same length.

The string s will be shuffled such that the 
character at the ith position moves to indices[i] 
in the shuffled string.

Return the shuffled string.
{Fore.RESET}
{Fore.RED}=================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1528.py -s "codeleet" --indices 4 5 6 7 0 2 1 3
	>>> "leetcode"

Example 2:
	$ python3 l-1528.py -s "abc" --indices 0 1 2
	>>> "abc"

Example 3:
	$ python3 l-1528.py -s "aiohn" --indices 3 1 4 2 0
	>>> "nihao"

Example 4:
	$ python3 l-1528.py -s "aaiougrt" --indices 4 0 2 6 7 3 1 5
	>>> "arigatou"

Example 5:
	$ python3 l-1528.py -s "art" --indices 1 0 2
	>>> "rat"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.indices and args.s:
		
		# Check if indices is correct
		temp = [x for x in range(len(args.s[0]))]
		if sorted(args.indices) == temp:
			result = Solution().restoreString(args.s[0], args.indices)
			print(result)

		else:
			print(f'{Fore.RED}[!] Indices incorrect{Fore.RESET}\n[?] For help message enter: python3 l-1528.py --help')
		

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()