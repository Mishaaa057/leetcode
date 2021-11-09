# 1684. Count the Number of Consistent Strings

from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-a', '--allowed', nargs=1, type=str, help='Allowed distinct characters')
	parser.add_argument('-w', '--words', nargs='+', type=str, help='Array of strings')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        counter = 0
        for word in words:
            temp = True
            for el in word:
                if el not in allowed:
                    temp = False
            
            if temp:
                counter += 1
        
        return counter 


def main():
	descr = f'''
{Fore.RED}================================================{Fore.RESET}
{Fore.GREEN}
	# 1684. Count the Number of 
	    Consistent Strings

You are given a string allowed consisting of 
distinct characters and an array of strings 
words. A string is consistent if all 
characters in the string appear in 
the string allowed.

Return the number of consistent strings 
in the array words.
{Fore.RESET}
{Fore.RED}================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1684.py --allowed "ab" --words "ad" "bd" "aaab" "baa" "badab"
	>>> 2
{Fore.GREEN}
	Explanation: Strings "aaab" and "baa" are consistent 
		since they only contain characters 'a' and 'b'.
{Fore.RESET}
Example 2:
	$ python3 l-1684.py --allowed "abc" --words "a" "b" "c" "ab" "ac" "bc" "abc"
	>>> 7
{Fore.GREEN}
	Explanation: All strings are consistent.
{Fore.RESET}
Example 3:
	$ python3 l-1684.py --allowed "cad" --words "cc" "acd" "b" "ba" "bac" "bad" "ac" "d"
	Output: 4
{Fore.GREEN}
	Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.allowed and args.words:
		result = Solution().countConsistentStrings(args.allowed[0], args.words)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
