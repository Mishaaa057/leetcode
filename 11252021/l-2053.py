# 2053. Kth Distinct String in an Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-a', '--array', type=str, nargs='+', help='Array of strings' )
	parser.add_argument('-k', type=int, nargs=1, help='An integer K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def kthDistinct(self, arr: list, k: int) -> str:
        lst = []        
        for index, el in enumerate(arr):
            
            
            if el not in arr[index+1:] and el not in arr[:index]:
                lst.append(el)
        
        if len(lst) >= k:
            return lst[k-1]
        else:
            return ''
	

def main():
	descr = f'''
{Fore.RED}==============================================================================={Fore.RESET}
{Fore.GREEN}
	# 2053. Kth Distinct String in an Array

A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth 
distinct string present in arr. If there are fewer than k distinct strings, 
return an empty string "".

Note that the strings are considered in the order in which they 
appear in the array.
{Fore.RESET}
{Fore.RED}==============================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-2053.py --array "d" "b" "c" "b" "c" "a" -k 2
	>>> "a"
{Fore.GREEN}
	Explanation:
	The only distinct strings in arr are "d" and "a".
	"d" appears 1st, so it is the 1st distinct string.
	"a" appears 2nd, so it is the 2nd distinct string.
	Since k == 2, "a" is returned. 
{Fore.RESET}
Example 2:
	$ python3 l-2053.py --array "aaa" "aa" "a" -k 1
	>>> "aaa"
{Fore.GREEN}
	Explanation:
	All strings in arr are distinct, so the 1st string "aaa" is returned.
{Fore.RESET}
Example 3:
	$ python3 l-2053.py --array "a" "b" "a" -k 3
	>>> ""
{Fore.GREEN}
	Explanation:
	The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
{Fore.RESET}	
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.array and args.k:
		result = Solution().kthDistinct(args.array, args.k[0])
		print(f'"{result}"')

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()