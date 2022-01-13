# 482. License Key Formatting

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', type=str, nargs=1, help='String S')
	parser.add_argument('-k', type=int, nargs=1, help='Integer K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        
        lst = []
        while len(s) > k:
            lst.append(s[-k:])
            s = s[:-k]
        
        result = ''
        
        if s:
            result += s
        for el in lst[::-1]:
            if result:
                result += f'-{el}'
            else:
                result += el
        return result.upper()


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 482. License Key Formatting

You are given a license key represented as a string s that consists
of only alphanumeric characters and dashes. The string is separated
into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains
exactly k characters, except for the first group, which could be
shorter than k but still must contain at least one character.
Furthermore, there must be a dash inserted between two groups, and
you should convert all lowercase letters to uppercase.

Return the reformatted license key.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0482.py -s "5F3Z-2e-9-w" -k 4
	>>> "5F3Z-2E9W"
{Fore.GREEN}
	Explanation:
	The string s has been split into two parts, each part has 4
	characters.
	Note that the two extra dashes are not needed and can be removed.
{Fore.RESET}
Example 2:
	$ python3 l-0482.py -s "2-5g-3-J" -k 2
	>>> "2-5G-3J"
{Fore.GREEN}
	Explanation:
	The string s has been split into three parts, each part has
	2 characters except the first part as it could be shorter as
	mentioned above.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.s and args.k:
		result = Solution().licenseKeyFormatting(args.s[0], args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()