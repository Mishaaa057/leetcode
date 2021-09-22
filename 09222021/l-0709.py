# 709. To Lower Case

from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--string', '-s', type=str, metavar='s',
		nargs=1, help='Some string')
	parser.add_argument('--description', '-d', action='store_true',
		help='Show description')
	parser.add_argument('--example', '-e', action='store_true',
		help='Show example')

	return parser 


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


def Main():
	descr = f'''
{Fore.RED}========================================================{Fore.RESET}
	{Fore.GREEN}# 709. To Lower Case

Given a string s, return the string after replacing 
every uppercase letter with the same lowercase letter.{Fore.RESET}
{Fore.RED}========================================================{Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0709.py --string "Hello"
	>>> "hello"

Example 2:
	$ python3 l-0709.py --string "here"
	>>> "here"

Example 3:
	$ python3 l-0709.py --string "LOVELY"
	>>> "lovely"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().toLowerCase(args.string[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()
