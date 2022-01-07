# 944. Delete Columns to Make Sorted

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--strs', type=str, nargs='+', help='List of strings')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def minDeletionSize(self, strs: list) -> int:
        lst = []
        
        for index, el in enumerate(strs[0]):
            temp = ''
            for el2 in strs:
                temp += el2[index]
            lst.append(temp)
        
        counter = 0 
        for index, el in enumerate(lst):
            if ''.join(sorted(el)) != el:
                counter += 1
        
        return counter
    
def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 944. Delete Columns to Make Sorted

You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line,
making a grid. For example, strs = ["abc", "bce", "cae"] can be
	arranged as:
		abc
		bce
		cae
You want to delete the columns that are not sorted lexicographically.
In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2
('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so
you would delete column 1.

Return the number of columns that you will delete.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0944.py --strs "cba" "daf" "ghi"
	>>> 1
{Fore.GREEN}
	Explanation: The grid looks as follows:
	  cba
	  daf
	  ghi
	Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
{Fore.RESET}
Example 2:
	$ python3 l-0944.py --strs "a" "b"
	>>> 0
{Fore.GREEN}
	Explanation: The grid looks as follows:
	  a
	  b
	Column 0 is the only column and is sorted, so you will not delete any columns.
{Fore.RESET}
Example 3:
	$ python3 l-0944.py --strs "zyx" "wvu" "tsr"
	>>> 3
{Fore.GREEN}
	Explanation: The grid looks as follows:
	  zyx
	  wvu
	  tsr
	All 3 columns are not sorted, so you will delete all 3.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.strs:
		result = Solution().minDeletionSize(args.strs)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()