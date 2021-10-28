# 189. Rotate Array


import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', metavar='n', help='Integer Array')
	parser.add_argument('-k', type=int, nargs=1, metavar='n', help='K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Check if k < nums
        while len(nums) < k:
            k = k - len(nums) 
        
        new_list = []
        
        # Swap last k elements with elements before
        end = nums[-k:]
        start = nums[:-k]
        
        new_list += end
        new_list += start

        # Rewrite list Nums
        for index, el in enumerate(new_list):
            nums[index] = el

        return nums


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 189. Rotate Array

Given an array, rotate the array to the right 
by k steps, where k is non-negative
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0189.py --nums 1 2 3 4 5 6 7 -k 3
	>>> [5,6,7,1,2,3,4]
{Fore.GREEN}
	Explanation:
	rotate 1 steps to the right: [7,1,2,3,4,5,6]
	rotate 2 steps to the right: [6,7,1,2,3,4,5]
	rotate 3 steps to the right: [5,6,7,1,2,3,4]
{Fore.RESET}
Example 2:
	$ python3 l-0189.py --nums -1 -100 3 99 -k  2
	>>> [3,99,-1,-100]
{Fore.GREEN}
	Explanation: 
	rotate 1 steps to the right: [99,-1,-100,3]
	rotate 2 steps to the right: [3,99,-1,-100]
{Fore.RESET}
	''' 

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums and args.k:
		result = Solution().rotate(args.nums, args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()