# 2114. Maximum Number of Words Found in Sentences

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--sentences', type=str, nargs='+', help='Sentences')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 

class Solution:
    def mostWordsFound(self, sentences: list) -> int:
        words_num = []
        
        for sentence in sentences:
            words_num.append(len(sentence.split()))
        
        return max(words_num)


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 2114. Maximum Number of Words Found in Sentences

A sentence is a list of words that are separated by a single space
with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i]
represents a single sentence.

Return the maximum number of words that appear in a single sentence.
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-2114.py --sentences "alice and bob love leetcode" "i think so too" "this is great thanks very much"
	>>> 6
{Fore.GREEN}
	Explanation: 
		- The first sentence, "alice and bob love leetcode", has 5 words in total.
		- The second sentence, "i think so too", has 4 words in total.
		- The third sentence, "this is great thanks very much", has 6 words in total.
		Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
{Fore.RESET}
Example 2:
	$ python3 l-2114.py --sentences "please wait" "continue to fight" "continue to win"
	>>> 3
{Fore.GREEN}
	Explanation: 
		It is possible that multiple sentences contain the same number of words. 
		In this example, the second and third sentences (underlined) have the same number of words.
{Fore.RESET}
		'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.sentences:
		result = Solution().mostWordsFound(args.sentences)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
