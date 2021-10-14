# 2000. Reverse Prefix of Word


import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-w', '--word', metavar='"word"', nargs=1, type=str, help='Word')
	parser.add_argument('-ch', '--character', metavar='x', nargs=1, type=str, help='Character')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # check if character in word
        if ch not in word:
            return word
        
        # get prefix index
        for index, el in enumerate(word):
            if el == ch:
                pref_index = index
                break
        
        # get prefix and other
        prefix = ''
        other = ''
        for index, letter in enumerate(word):
            if index <= pref_index:
                prefix += letter
            else:
                other += letter
                
        # reverse prefix
        new_prefix = ''
        for el in prefix:
            new_prefix = el + new_prefix
        
        # build and return result
        result = new_prefix + other
        return result


def main():
	descr = f'''
{Fore.RED}===================================================={Fore.RESET}
{Fore.GREEN}
	# 2000. Reverse The Prefix of Word

Given a 0-indexed string word and a character ch, 
reverse the segment of word that starts at index 0
 and ends at the index of the first occurrence 
 of ch (inclusive). If the character ch does 
 not exist in word, do nothing.

For example: 
	if word = "abcdefd" and ch = "d", 
	then you should reverse the segment that
	starts at 0 and ends at 3 (inclusive). 
	The resulting string will be "dcbaefd".

Return the resulting string.
{Fore.RESET}
{Fore.RED}===================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-2000.py --word "abcdefd" -ch "d"
	>>> "dcbaefd"
{Fore.GREEN}
	Explanation: The first occurrence of "d" is at index 3. 
	Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
{Fore.RESET}
Example 2:
	$ python3 l-2000.py --word "xyxzxe" -ch "z"
	>>> "zxyxxe"
{Fore.GREEN}
	Explanation: The first and only occurrence of "z" is at index 3.
	Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
{Fore.RESET}
Example 3:
	$ python3 l-2000.py --word "abcd" -ch "z"
	>>> "abcd"
{Fore.GREEN}
	Explanation: "z" does not exist in word.
	You should not do any reverse operation, the resulting string is "abcd".
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()


	if args.word and args.character:
		result = Solution().reversePrefix(args.word[0], args.character[0])
		print(f'"{result}"')

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
