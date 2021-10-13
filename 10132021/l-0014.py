# 14. Longest Common Prefix


import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--strs', type=str, nargs='+', metavar='"word"', help='Array of strings')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        prefix = ''
        
        if len(strs) > 1:
            # get first word
            word = strs[0]
            
            temp = ''
            for index, el in enumerate(word):
                # check for the symbol in other words
                temp += el
                for word1 in strs:
                    if len(word1) >= len(temp):
                        if word1[index] != el:
                            return prefix # if there now symbol in other words: return prew symbols
                    else:
                        
                        return prefix
                prefix = temp
            return prefix 
                
        else:
            return strs[0]


def main():
	descr = f'''
{Fore.RED}=============================================={Fore.RESET}
{Fore.GREEN}
	# 14. Longest Common Prefix

Write a function to find the longest common 
prefix string amongst an array of strings.

If there is no common prefix, return an 
empty string "".
{Fore.RED}=============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0014.py --strs "flower" "flow" "flight"
	>>> "fl"

Example 2:
	$ python3 l-0014.py --strs "dog" "racecar" "car"
	>>> ""
{Fore.GREEN}
	Explanation: There is no common prefix among the input strings.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.strs:
		result = Solution().longestCommonPrefix(args.strs)
		print(f'"{result}"')

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
