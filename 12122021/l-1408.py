# 1408. String Matching in an Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-ws', '--words', type=str, nargs='+', help='Words array')
	parser.add_argument('-d', '--description', action='store_true', help='Show desription')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def stringMatching(self, words: list) -> list:
        result = []
        for index, word in enumerate(words):
            
            for index2, word2 in enumerate(words):
                if index != index2:
                    if word in word2:
                        if word not in result:
                            result.append(word)
        
        return result


def main():
	descr = f'''
{Fore.RED + ('='*70)+ Fore.RESET}
{Fore.GREEN}
	# 1408. String Matching in an Array

iven an array of string words. Return all strings in words which is 
substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained 
removing some characters to left and/or right side of words[j].
{Fore.RESET}
{Fore.RED + ('='*70)+ Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1408.py --words "mass" "as" "hero" "superhero"
	>>> ["as","hero"]
{Fore.GREEN}
	Explanation: "as" is substring of "mass" and "hero" is 
	substring of "superhero".
	["hero","as"] is also a valid answer.
{Fore.RESET}
Example 2:
	$ python3 l-1408.py --words "leetcode" "et" "code"
	>>> ["et","code"]
{Fore.GREEN}
	Explanation: "et", "code" are substring of "leetcode".
{Fore.RESET}
Example 3:
	$ python3 l-1408.py --words "blue" "green" "bu"
	>>> []
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.words:
		result = Solution().stringMatching(args.words)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
	