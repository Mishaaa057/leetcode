# 13. Roman to Integer


import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-r', '--roman', type=str, nargs=1, metavar='"XII"', help='Roman number')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


symbols = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        # expand by number to roman list
        roman_lst = []
        
        string = ''
        for el in s:
            if el in string:
                string += el
            else:
                roman_lst.append(string)
                string = el
        roman_lst.append(string)
        roman_lst.remove(roman_lst[0])
                     
        values = []
        
        pass_lst = []
        for index, el in enumerate(roman_lst):
            if index not in pass_lst:
                # check if value < 5, 10, 50, 100 ...
                if index <= len(roman_lst) - 2:
                    if len(el) == 1 and len(roman_lst[index + 1]) == 1:
                        this_value = symbols[el]

                        next_value = symbols[roman_lst[index + 1]]

                        if this_value < next_value:

                            pass_lst.append(index + 1)
                            pass_lst.append(index)
                            values.append(next_value - this_value)
                            
                # check if value consist of several characters
                if len(el) > 1:
                    value = 0
                    for i in el:
                        value += symbols[i]
                    values.append(value)
                
                # check if single character
                if index not in pass_lst:
                    if len(el) == 1:
                        values.append(symbols[el])

        return sum(values)


def main():
	descr = f'''
{Fore.RED}========================================================================{Fore.RESET}
{Fore.GREEN}
		# 13. Roman To Integer

Roman numerals are represented by seven different 
symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two 
one's added together. 12 is written as XII, which is simply 
X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from 
left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is 
before the five we subtract it making four. The same principle 
applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

	I can be placed before V (5) and X (10) to make 4 and 9. 
	X can be placed before L (50) and C (100) to make 40 and 90. 
	C can be placed before D (500) and M (1000) to make 400 and 900.
	Given a roman numeral, convert it to an integer.
{Fore.RESET}
{Fore.RED}========================================================================{Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0013.py -r "III"
	>>> 3

Example 2:
	$ python3 l-0013.py -r "IV"
	>>> 4

Example 3:
	$ python3 l-0013.py -r "IX"
	>>> 9

Example 4:
	$ python3 l-0013.py --roman "LVIII"
	>>> 58

Example 5:
	$ python3 l-0013.py --roman "MCMXCIV"
	>>> 1994
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.roman:
		result = Solution().romanToInt(args.roman[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()