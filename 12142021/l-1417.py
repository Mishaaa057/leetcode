# 1417. Reformat The String

import argparse 
from colorama import Fore 


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--string', type=str, nargs=1, help='String')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        
        for el in s:
            try:
                el = int(el)
                digits.append(str(el))
            except:
                letters.append(el)
        if len(s) == 1:
            return s

        l = len(letters)
        d = len(digits)
        if l == 0 or d == 0 or l >= d+2 or d >= l+2 :
            return ''
        
        
        result = ''
        if len(digits) > len(letters):
            letters, digits = digits, letters
        
        while letters or digits:
            result += letters[0]
            letters.remove(letters[0])
            if digits:
                result += digits[0]
                digits.remove(digits[0])
        

        return result


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 1417. Reformat The String

Given alphanumeric string s. (Alphanumeric string is a string 
consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is 
followed by another letter and no digit is followed by another digit. 
That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is 
impossible to reformat the string.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1417.py --string "a0b1c2"
	>>> "0a1b2c"
{Fore.GREEN}
	Explanation: No two adjacent characters have the same 
	type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
{Fore.RESET}
Example 2:
	$ python3 l-1417.py --string "leetcode"
	>>> ""
{Fore.GREEN}
	Explanation: "leetcode" has only characters 
	so we cannot separate them by digits.
{Fore.RESET}
Example 3:
	$ python3 l-1417.py --string "1229857369"
	>>> ""
{Fore.GREEN}
	Explanation: "1229857369" has only digits so we cannot 
	separate them by characters.
{Fore.RESET}
Example 4:
	$ python3 l-1417.py --string "covid2019"
	>>> "c2o0v1i9d"

Example 5:
	$ python3 l-1417.py --string "ab123"
	>>> "1a2b3"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().reformat(args.string[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()

