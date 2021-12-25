# 1437. Check If All 1's Are at Least Length K Places Away

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Integer Array Nums')
	parser.add_argument('-k', type=int, nargs=1, help='Integer K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def kLengthApart(self, nums: list, k: int) -> bool:
        if k == 0:
            return True
        
        indexes = []
        
        for index, el in enumerate(nums):
            if el == 1:
                indexes.append(index+1)
        
        for index1, el1 in enumerate(indexes):
            for index2, el2 in enumerate(indexes[index1+1:]):
                if k > (el2 - el1 - 1):
                    return False
        return True


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 1437. Check If All 1's Are at Least Length K Places Away

Given an binary array nums and an integer k, return true if all 1's
are at least k places away from each other, otherwise return false.
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1437.py --nums 1 0 0 0 1 0 0 1 -k 2
	>>> True
{Fore.GREEN}
	Explanation:
		Each of the 1s are at least 2 places away from each other.
{Fore.RESET}
Example 2:
	$ python3 l-1437.py --nums 1 0 0 1 0 1 -k 2
	>>> False
{Fore.GREEN}
	Explanation:
	The second 1 and third 1 are only one apart from each other.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums and args.k:
		result = Solution().kLengthApart(args.nums, args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
