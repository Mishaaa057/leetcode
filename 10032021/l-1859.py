# 1859. Sorting the Sentence


from colorama import Fore as F
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--string', metavar='s', nargs='+', type=str, help='String')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def sortSentence(self, s: str) -> str:
        dct = {}
        lst = s.split(' ')
        
        for el in lst:
            num = int(el[-1:])
            el = el[:-1]
            
            if num not in dct:
                dct[num] = el
        
        result = ''
        for i in range(1, len(dct) + 1):
            if i == len(dct):
                result += dct[i]
            else:
                result += dct[i] + ' '
        return result
        


def main():
	descr = f'''
{F.RED}===================================================================={F.RESET}
{F.GREEN}		
		# 1859. Sorting the Sentencd
A sentence is a list of words that are separated by a single space with 
no leading or trailing spaces. Each word consists of lowercase and 
uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to 
each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as 
"sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".

Given a shuffled sentence s containing no more than 9 words, reconstruct 
and return the original sentence.
{F.RESET}
{F.RED}===================================================================={F.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-1859.py -s "is2 sentence4 This1 a3"
	>>> "This is a sentence"

Example 2:
	$ python3 l-1859.py -s "Myself2 Me1 I4 and3"
	>>> "Me Myself and I"

	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().sortSentence(args.string[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()