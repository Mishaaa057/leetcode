# 796. Rotate String

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--string', type=str, nargs=1, metavar='somestring', help='String')
	parser.add_argument('-g', '--goal', type=str, nargs=1, metavar='somestring', help='Goal')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for k in range(len(s)):
            new_string = ''

            # Swap last k elements with elements before
            end = s[-k:]
            start = s[:-k]

            new_string += end
            new_string += start
            
            if new_string == goal:
                return True
        
        return False


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 796. Rotate String

Given two strings s and goal, return 
true if and only if s can become goal 
after some number of shifts on s.

A shift on s consists of moving the 
leftmost character of s to 
the rightmost position.

	For example, if s = "abcde", 
	then it will be "bcdea" after one shift.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0796.py --string "abcde" --goal "cdeab"
	>>> True

Example 2:
	$ python3 l-0796.py --string "abcde" --goal "abced"
	>>> False
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string and args.goal:
		result = Solution().rotateString(args.string[0], args.goal[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()