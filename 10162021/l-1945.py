# 1945. Sum of Digits of String After Convert


import argparse
import string
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--string',nargs=1, type=str, help='String')
	parser.add_argument('-k',nargs=1, metavar='n', type=int, help='Integer K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description') 
	parser.add_argument('-e', '--example', action='store_true', help='Show example') 
	
	return parser


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet_string = list(string.ascii_lowercase)
        
        dct = {}
        for index, el in enumerate(alphabet_string):
            index += 1
            dct[el] = index
        
        str_number = ''
        for el in s:
            str_number += str(dct[el])
        
        for i in range(k):
            res = 0
            for el in str_number:
                res += int(el)
            
            str_number = str(res)
        
        return int(str_number)
        
        
def main():
	descr = f'''
{Fore.RED}=================================================================={Fore.RESET}
{Fore.GREEN}
	# 1945. Sum of Digits of String After Convert

You are given a string s consisting of lowercase English 
letters, and an integer k.

First, convert s into an integer by replacing each letter 
with its position in the alphabet (i.e., replace 'a' 
with 1, 'b' with 2, ..., 'z' with 26). Then, transform the
integer by replacing it with the sum of its digits. Repeat 
the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer 
would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8

Return the resulting integer after performing the operations 
described above.
{Fore.RESET}
{Fore.RED}=================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1945.py --string "iiii" -k 1
	>>> 36
{Fore.GREEN}
	Explanation: The operations are as follows:
		- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
		- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
	Thus the resulting integer is 36.
{Fore.RESET}
Example 2:
	$ python3 l-1945.py --string "leetcode" -k 2
	>>> 6
{Fore.GREEN}	
	Explanation: The operations are as follows:
		- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
		- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
		- Transform #2: 33 ➝ 3 + 3 ➝ 6
	Thus the resulting integer is 6.
{Fore.RESET}
Example 3:
	$ python3 l-1945.py --string "zbax" -k 2
	>>> 8
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string and args.k:
		result = Solution().getLucky(args.string[0], args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
