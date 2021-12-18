# 1299. Replace Elements with Greatest Element on Right Side

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-a', '--array', type=str, nargs='+', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def replaceElements(self, arr: list) -> list:
        for index, el in enumerate(arr):
            right = arr[index+1:]
            if right != []:
                arr[index] = max(right)
            else:
                arr[index] = -1
        
        return arr
    

def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the 
greatest element among the elements to its right, and replace the 
last element with -1.

After doing so, return the array.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1299.py --array 17 18 5 4 6 1
	>>> [18,6,6,6,1,-1]
{Fore.GREEN}
	Explanation: 
		- index 0 --> the greatest element to the right of index 0 is
		index 1 (18).
		- index 1 --> the greatest element to the right of index 1 is
		index 4 (6).
		- index 2 --> the greatest element to the right of index 2 is
		index 4 (6).
		- index 3 --> the greatest element to the right of index 3 is
		index 4 (6).
		- index 4 --> the greatest element to the right of index 4 is
		index 5 (1).
		- index 5 --> there are no elements to the right of index 5,
		so we put -1.

{Fore.RESET}
Example 2:
	$ python3 l-1299.py --array 400
	>>> [-1]
{Fore.GREEN}
	Explanation: There are no elements to the right of index 0.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.array:
		result = Solution().replaceElements(args.array)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()