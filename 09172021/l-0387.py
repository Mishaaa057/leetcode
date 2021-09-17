# 387. First Unique Character in a String


from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--string', '-s', type=str, metavar='s',
		nargs=1, help='String')
	parser.add_argument('--description', '-d', 
		action='store_true', help='Show description')
	parser.add_argument('--example', '-e',
		action='store_true', help='Show example')

	return parser


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        
        for index, el in enumerate(s):
            if el not in dct:
                dct[el] = [index]
            else:
                dct[el].append(index)
            
        for key in dct:
            if len(dct[key]) == 1:
                return dct[key][0]
        
        return -1


def Main():
	descr = f'''
{Fore.RED}=================================================={Fore.RESET}
	{Fore.GREEN}# 387. First Unique Character in a String


Given a string s, find the first non-repeating 
character in it and return its index. 
If it does not exist, return -1.{Fore.RESET}
{Fore.RED}=================================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0387.py --string 'leetcode'
	>>> 0

Example 2:
	$ python3 l-0387.py --string "loveleetcode"
	>>> 2

Example 3:
	$ python3 l-0387.py --string "aabb"
	>>> -1
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().firstUniqChar(args.string[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()