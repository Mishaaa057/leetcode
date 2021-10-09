# 290. Word Pattern


from colorama import Fore
import argparse


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-p', '--pattern', type=str, metavar='"abba"', nargs=1, help='Pattern')
	parser.add_argument('-s', '--string', type=str, metavar='"cat dog dog cat"', nargs=1, help='string S')	
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dct = {}
        word_lst = s.split()
        
        # check for length
        if len(pattern) != len(word_lst):
            return False
        
        # build dictionary
        for index, el in enumerate(pattern): 
            word = word_lst[index]
            if el not in dct:
                if word not in dct.values():
                    dct[el] = word
                else:
                    return False
                
        # check similarity dictionary and string
        for index, el in enumerate(pattern):
            if dct[el] != word_lst[index]:
                return False
        return True


def main():
	descr = f'''
{Fore.RED}======================================================{Fore.RESET}
{Fore.GREEN}
		# 290. Word Pattern
Given a pattern and a string s, find if s follows 
the same pattern.

Here follow means a full match, such that there is a 
bijection between a letter in pattern and a non-empty 
word in s.
{Fore.RESET}
{Fore.RED}======================================================{Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0290.py --pattern "abba" --string "dog cat cat dog"
	>>> True

Example 2:
	$ python3 l-0290.py --pattern "abba" --string "dog cat cat fish"
	>>> False

Example 3:
	$ python3 l-0290.py --pattern "aaaa" --string "dog cat cat dog"
	>>> False

Example 4:
	$ python3 l-0290.py --pattern "abba" --string "dog dog dog dog"
	>>> False
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.pattern and args.string:
		result = Solution().wordPattern(args.pattern[0], args.string[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
