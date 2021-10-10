# 1832. Check if the Sentence Is Pangram


import argparse
import string
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--sentence', type=str, nargs=1, metavar='"sentence"', help='String' )
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = string. ascii_lowercase
        
        for el in alphabet:
            if el not in sentence:
                return False
        return True


def main():
	descr = f'''
{Fore.RED}==========================================================={Fore.RESET}
{Fore.GREEN}
	# 1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of 
the English alphabet appears at least once.

Given a string sentence containing only lowercase English 
letters, return true if sentence is a pangram, or false 
otherwise
{Fore.RESET}
{Fore.RED}==========================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1832.py --sentence "thequickbrownfoxjumpsoverthelazydog"
	>>> True
{Fore.GREEN}
	Explanation: sentence contains at least one of every letter of the English alphabet.
{Fore.RESET}
Example 2:
	$ python3 l-1832.py --sentence "leetcode"
	>>> False
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.sentence:
		result = Solution().checkIfPangram(args.sentence[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
	