# 541. Reverse String II

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--string', type=str, nargs=1, help='String')
	parser.add_argument('-k', type=int, nargs=1, help='Integer K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = []
        temp = []
        
        for index, el in enumerate(s):
            index += 1
            #print(index % k == 0)
            if not index % k == 0:
                temp.append(el)
            else:
                temp.append(el)
                lst.append(temp)
                temp = []
                
        if not len(s) % k == 0:
            n = len(s) % k
            lst.append(list(s[-n:]))

        result = ''

        # reverse each element in lst
        for index, el in enumerate(lst):
            if index % 2 == 0:
                el = el[::-1]
            
            string = ''.join(el)
            result += string
            
        return result


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 541. Reverse String II

Given a string s and an integer k, reverse the first k characters for
every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If
there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0541.py --string "abcdefg" -k 2
	>>> "bacdfeg"

Example 2:
	$ python3 l-0541.py --string "abcd" -k 2
	>>> "bacd"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string and args.k:
		result = Solution().reverseStr(args.string[0], args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()

