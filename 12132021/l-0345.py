# 345. Reverse Vowels of a String

import argparse
from colorama import Fore 


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--string', type=str, nargs=1, help='String')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        lst = []
        pattern = []
        
        # Get vowels from string and generate pattern
        for index, el in enumerate(s):
            if el.lower() in vowels:
                pattern.append(None)
                lst.append(el)
            else:
                pattern.append(el)
        
        # Reverse vowels list
        lst = lst[::-1]
        
        # Set reversed vowels into pattern
        for index, el in enumerate(pattern):
            if not el:
                pattern[index] = lst[0]
                lst.remove(lst[0])
        
        # Build result string
        result = ''.join(pattern)
        return result


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and 
return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear 
in both cases.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0345.py --string "hello"
	>>> "holle"

Example 2:
	$ python3 l-0345.py --string "leetcode"
	>>> "leotcede"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().reverseVowels(args.string[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
