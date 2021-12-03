# 1394. Find Lucky Integer in an Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--arr', type=int, nargs='+', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def findLucky(self, arr: list) -> int:
        lucky_numbers = []
        
        dct = {}
        
        # Generate dictionary with number and how much times that number in array
        for index, el in enumerate(arr):
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        
        # Get from dictionary lucky numbers
        for key in dct:
            if key == dct[key]:
                lucky_numbers.append(key)
        
        # Check if lucky numbers array not empty & return max lucky namber
        if lucky_numbers:
            return max(lucky_numbers)
        else:
            return -1


def main():
	descr = f'''
{Fore.RED}===================================================================={Fore.RESET}
{Fore.GREEN}
	# 1394. Find Lucky Integer in an Array

Given an array of integers arr, a lucky integer is an integer 
which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky 
integers return the largest of them. If there is no lucky 
integer return -1.
{Fore.RESET}
{Fore.RED}===================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1394.py --arr 2 2 3 4
	>>> 2
{Fore.GREEN}
	Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
{Fore.RESET}
Example 2:
	$ python3 l-1394.py --arr 1 2 2 3 3 3
	>>> 3
{Fore.GREEN}
	Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
{Fore.RESET}
Example 3:
	$ python3 l-1394.py --arr 2 2 2 3 3
	>>> -1
{Fore.GREEN}
	Explanation: There are no lucky numbers in the array.
{Fore.RESET}
Example 4:
	$ python3 l-1394.py --arr 5
	>>> -1

Example 5:
	$ python3 l-1394.py --arr 7 7 7 7 7 7 7
	>>> 7
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.arr:
		result = Solution().findLucky(args.arr)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()