# 1619. Mean of Array After Removing Some Elements

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-a', '--array', type=int, nargs='+', help='Array of integers')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def trimMean(self, arr: list) -> float:
        n = (5 * (len(arr))/ 100)
        
        if n >= 1:
            for i in range(int(n)):
                arr.remove(max(arr))
                arr.remove(min(arr))
        
        return sum(arr) / len(arr)


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 1619. Mean of Array After Removing Some Elements

Given an integer array arr, return the mean of the remaining integers 
after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1619.py --array 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3
	>>> 2.00000
{Fore.GREEN}
Explanation: After erasing the minimum and the maximum values of this array, 
all elements are equal to 2, so the mean is 2.
{Fore.RESET}
Example 2:
	$ python3 l-1619.py --array 6 2 7 5 1 2 0 3 10 2 5 0 5 5 0 8 7 6 8 0
	>>> 4.00000
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.array:
		result = Solution().trimMean(args.array)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()