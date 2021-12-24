# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--sentence', type=str, nargs=1, help='Sentence')
	parser.add_argument('-sw', '--searchWord', type=str, nargs=1, help='Search Word')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if searchWord in sentence:
            lst = sentence.split(' ')
            for index, el in enumerate(lst):
                if len(searchWord) <= len(el):
                    if searchWord == el[:len(searchWord)]:
                        return index+1
        return -1


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

Given a sentence that consists of some words separated by a single
space, and a searchWord, check if searchWord is a prefix of any word
in sentence.

Return the index of the word in sentence (1-indexed) where searchWord
is a prefix of this word. If searchWord is a prefix of more than one
word, return the index of the first word (minimum index). If there is
no such word return -1.

A prefix of a string s is any leading contiguous substring of s.
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1455.py --sentence "i love eating burger" --searchWord "burg"
	>>> 4
{Fore.GREEN}
	Explanation: 
	"burg" is prefix of "burger" which is the 4th word in the sentence.
{Fore.RESET}
Example 2:
	$ python3 l-1455.py --sentence "this problem is an easy problem" --searchWord "pro"
	>>> 2
{Fore.GREEN}
	Explanation:
	"pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, 
	but we return 2 as it's the minimal index.
{Fore.RESET}
Example 3:
	$ python3 l-1455.py --sentence "i am tired" --searchWord "you"
	>>> -1
{Fore.GREEN}
	Explanation:
	"you" is not a prefix of any word in the sentence.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.sentence and args.searchWord:
		result = Solution().isPrefixOfWord(args.sentence[0], args.searchWord[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
