# 4. Median of Two Sorted Arrays
# Difficulty - [Hard]

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n1', '--nums1', type=int, nargs='+', metavar='N', help='Array of Integers 1')
	parser.add_argument('-n2', '--nums2', type=int, nargs='+', metavar='N', help='Array of Integers 2')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Generate one array
        nums = nums1 + nums2
        
        # Sort that array
        nums = sorted(nums)
        
        # If lenght array is not pair
        if len(nums) % 2 != 0:
            return (nums[len(nums) // 2])
        
        # If lenght array is pair
        else:
            a = nums[(len(nums) // 2) - 1] # [1, (2), 3, 4]; a = 2
            b = nums[(len(nums) // 2)]     # [1, 2, (3), 4]; b = 3
            
            return (a + b) / 2 # Get median


def main():
	descr = f'''
{Fore.RED}============================================={Fore.RESET}
{Fore.GREEN}
	# 4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 
of size m and n respectively, return the 
median of the two sorted arrays.

The overall run time complexity should 
be O(log (m+n)).
{Fore.RESET}
{Fore.RED}============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0004.py --nums1 1 3  --nums2 2
	>>> 2.00000
{Fore.GREEN}
	Explanation: merged array = [1,2,3] and median is 2.
{Fore.RESET}
Example 2:
	$ python3 l-0004.py --nums1 1 2 --nums2 3 4
	>>> 2.50000
{Fore.GREEN}
	Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
{Fore.RESET}
Example 3:
	$ python3 l-0004.py --nums1 0 0 --nums2 0 0 
	>>> 0.00000
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums1 and args.nums2:
		result = Solution().findMedianSortedArrays(args.nums1, args.nums2)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__ == "__main__":
	main()