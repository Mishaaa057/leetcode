# 1816. Truncate Sentence

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', type=str, nargs=1, help='Sentence')
	parser.add_argument('-k', type=int, nargs=1, help='Integer K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words_list = s.split(' ')
        
        result_string = ''
        
        for word in words_list[:k]:
            result_string += f'{word} '
        return result_string.strip()


def main():
	descr = f'''
{Fore.RED}========================================================={Fore.RESET}
{Fore.GREEN}
	# 1816. Truncate Sentence

A sentence is a list of words that are separated by a 
single space with no leading or trailing spaces. Each 
of the words consists of only uppercase and lowercase 
English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world 
hello world" are all sentences.

You are given a sentence s and an integer k. You want 
to truncate s such that it contains only the first k 
words. Return s after truncating it.
{Fore.RESET}
{Fore.RED}========================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1816.py -s "Hello how are you Contestant" -k 4
	>>> "Hello how are you"
{Fore.GREEN}
	Explanation:
	The words in s are ["Hello", "how" "are", "you", "Contestant"].
	The first 4 words are ["Hello", "how", "are", "you"].
	Hence, you should return "Hello how are you".
{Fore.RESET}
Example 2:
	$ python3 l-1816.py -s "What is the solution to this problem" -k 4
	>>> "What is the solution"
{Fore.GREEN}
	Explanation:
	The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
	The first 4 words are ["What", "is", "the", "solution"].
	Hence, you should return "What is the solution".
{Fore.RESET}
Example 3:
	$ python3 l-1816.py -s "chopper is not a tanuki" -k 5
	>>> "chopper is not a tanuki"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.s and args.k:
		result = Solution().truncateSentence(args.s[0], args.k[0])
		print(f'"{result}"')

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()