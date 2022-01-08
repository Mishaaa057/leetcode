# 6. Zigzag Conversion
# Difficulty - [Medium]

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', type=str, nargs=1, help='String')
	parser.add_argument('-nr', '--numRows', type=int, nargs=1, help='Num Rows')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        n = numRows - 2
        lines = []
        
        while len(s) > 0:
            if len(s) >= numRows:
                col = s[:numRows]
                s = s[numRows:]
            else:
                col = s
                s = ''
            lines.append(col)

            if len(s) >= n:
                line = s[:n]
                s = s[n:]
            else:
                line = s
                s = ''
            if line != '':
                line = '-' + line + ('-' * (n + 1 - len(line)))
                lines.append(line[::-1])
            
        result = ''
        for index, el in enumerate(lines[0]):
            for line in lines:
                if len(line) >= index+1:
                    if line[index] != '-':
                        result += line[index]
        
        return result
        

            
            
    
def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)
	P   A   H   N
	A P L S I I G
	Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given
a number of rows:

string convert(string s, int numRows);
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0006.py -s "PAYPALISHIRING" --numRows 3
	>>> "PAHNAPLSIIGYIR"

Example 2:
	$ python3 l-0006.py -s "PAYPALISHIRING" --numRows 4
	>>> "PINALSIGYAHRPI"
{Fore.GREEN}
	Explanation:
		P     I    N
		A   L S  I G
		Y A   H R
		P     I
{Fore.RESET}
Example 3:
	$ python3 l-0006.py -s "A" --numRows 1
	>>> "A"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.numRows and args.s:
		result = Solution().convert(args.s[0], args.numRows[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()