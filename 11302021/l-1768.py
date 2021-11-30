# 1768. Merge Strings Alternately

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-w1', '--word1', type=str, nargs=1, help='Word 1')
	parser.add_argument('-w2', '--word2', type=str, nargs=1, help='Word 2')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for index, el in enumerate(word1):
            result += el
            if len(word2) - 1 >= index:
                result += word2[index]
            if index == len(word1) - 1:
                result += word2[index+1:]
            
        return result


def main():
	descr = f'''
{Fore.RED}=================================================================={Fore.RESET}
{Fore.GREEN}
	# 1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by 
adding letters in alternating order, starting with word1. If a 
string is longer than the other, append the additional letters 
onto the end of the merged string.

Return the merged string.
{Fore.RESET}
{Fore.RED}=================================================================={Fore.RESET}
	'''
	
	example = f'''
Example 1:
	$ python3 l-1768.py --word1 "abc" --word2 "pqr"
	>>> "apbqcr"
{Fore.GREEN}
	Explanation: The merged string will be merged as so:
	word1:  a   b   c
	word2:    p   q   r
	merged: a p b q c r
{Fore.RESET}
Example 2:
	$ python3 l-1768.py --word1 "ab" --word2 "pqrs"
	>>> "apbqrs"
{Fore.GREEN}
	Explanation: Notice that as word2 is longer, "rs" is appended to the end.
	word1:  a   b 
	word2:    p   q   r   s
	merged: a p b q   r   s
{Fore.RESET}
Example 3:
	$ python3 l-1768.py --word1 "abcd" --word2 "pq"
	>>> "apbqcd"
{Fore.GREEN}
	Explanation: Notice that as word1 is longer, "cd" is appended to the end.
	word1:  a   b   c   d
	word2:    p   q 
	merged: a p b q c   d
{Fore.RESET}
	'''	

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.word1 and args.word2:
		result = Solution().mergeAlternately(args.word1[0], args.word2[0])
		print(f'"{result}"')

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()