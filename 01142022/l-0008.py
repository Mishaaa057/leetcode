# 8. String to Integer (atoi)

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', type=str, nargs=1, help='String S')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        digits = ''
        for el in s:
            if el.isdigit() or el == '-' or '+':
                digits += el
            else:
                break
        
        result = ''
        negative = False
        for index, el in enumerate(digits):
            if index == 0 and el == '-':
                negative = True
            elif index == 0 and el == '+':
                pass
            elif el.isdigit():
                result += el
            else:
                break
        
        if result.isdigit():
            result = int(result)
            if negative:
                result = result * (-1)
        else:
            result = 0
        
        if result > (2**31) - 1:
            result = (2**31) - 1
        elif result < -2**31:
            result = -2**31
        
        return result
        

def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
Implement the myAtoi(string s) function, which converts a string to a
32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
	Read in and ignore any leading whitespace.
	Check if the next character (if not already at the end of the
	string)is '-' or '+'. Read this character in if it is either.
	This determines if the final result is negative or
	positive respectively. Assume the result is positive if neither
	is present.
	Read in next the characters until the next non-digit character
	or the end of the input is reached. The rest of the string is
	ignored.
	Convert these digits into an integer (i.e. "123" -> 123, "0032"
	-> 32). If no digits were read, then the integer is 0. Change the
	sign as necessary (from step 2).
	If the integer is out of the 32-bit signed integer range [-231,
	231 - 1], then clamp the integer so that it remains in the range.
	Specifically, integers less than -231 should be clamped to -231,
	and integers greater than 231 - 1 should be clamped to 231 - 1.
	Return the integer as the final result.
Note:
	Only the space character ' ' is considered a whitespace
	character.
	Do not ignore any characters other than the leading whitespace
	or the rest of the string after the digits.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0008.py -s "42"
	>>> 42
{Fore.GREEN}
	Explanation:
	The underlined characters are what is read in, the caret is the
	current reader position.

	Step 1: "42" (no characters read because there is no leading whitespace)
	         ^
	Step 2: "42" (no characters read because there is neither a '-' nor '+')
	         ^
	Step 3: "42" ("42" is read in)
	           ^
	The parsed integer is 42.
	Since 42 is in the range [-231, 231 - 1], the final result is 42.
{Fore.RESET}
Example 2:
	$ python3 l-0008.py -s "   -42"
	>>> -42
{Fore.GREEN}
	Explanation:
	Step 1: "   -42" (leading whitespace is read and ignored)
	            ^
	Step 2: "   -42" ('-' is read, so the result should be negative)
	             ^
	Step 3: "   -42" ("42" is read in)
	               ^
	The parsed integer is -42.
	Since -42 is in the range [-231, 231 - 1], the final result is -42.
{Fore.RESET}
Example 3:
	$ python3 l-0008.py -s "4193 with words"
	>>> 4193
{Fore.GREEN}
	Explanation:
	Step 1: "4193 with words" (no characters read because there is no leading whitespace)
	         ^
	Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
	         ^
	Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
	             ^
	The parsed integer is 4193.
	Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.s:
		result = Solution().myAtoi(args.s[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
