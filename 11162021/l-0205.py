# 205. Isomorphic Strings

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', type=str, nargs=1, help='String 1 - S')
	parser.add_argument('-t', type=str, nargs=1, help='String 2 - T')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct = {}
        dct2 = {}
        
        for index, el in enumerate(s):
            if el not in dct:
                dct[el] = t[index]
        
            else:
                if dct[el] != t[index]:
                    return False
            
            if t[index] not in dct2:
                dct2[t[index]] = el
            else:
                if dct2[t[index]] != el:
                    return False

        return True


def main():
	descr = f'''
{Fore.RED}====================================================================={Fore.RESET}
{Fore.GREEN}
	# 205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s 
can be replaced to get t.

All occurrences of a character must be replaced with another 
character while preserving the order of characters. 
No two characters may map to the same character, but a 
character may map to itself.
{Fore.RESET}
{Fore.RED}====================================================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0205.py -s "egg" -t "add"
	>>> True

Example 2:
	$ python3 l-0205.py -s "foo" -t "bar"
	>>> False

Example 3:
	$ python3 l-0205.py -s "paper" -t "title"
	>>> True
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.s and args.t:
		result = Solution().isIsomorphic(args.s[0], args.t[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
