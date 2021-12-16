# 1160. Find Words That Can Be Formed by Characters

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-w', '--words', type=str, nargs='+', help='Words array')
	parser.add_argument('-ch', '--chars', type=str, nargs=1, help='Chars string')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def countCharacters(self, words: list, chars: str) -> int:
        result_lst = []
        lst = list(chars)
        for word in words:
            temp = lst.copy()
            
            for index, el in enumerate(word):
                
                if el in temp:
                    temp.remove(el)
                    if index == len(word) - 1:
                        result_lst.append(word)
                else:
                    break
                
            
        result = 0
        for el in result_lst:
            result += len(el)
            
        return result


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 1160. Find Words That Can Be Formed by 
				Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars 
(each character can only be used once).

Return the sum of lengths of all good strings in words.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1160.py --words "cat" "bt" "hat" "tree" --chars "atach"
	>>> 6
{Fore.GREEN}
	Explanation: The strings that can be formed are "cat" and "hat" 
	so the answer is 3 + 3 = 6.
{Fore.RESET}
Example 2:
	$ python3 l-1160.py --words "hello" "world" "leetcode" --chars "welldonehoneyr"
	>>> 10
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.words and args.chars:
		result = Solution().countCharacters(args.words, args.chars[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()