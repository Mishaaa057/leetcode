# 287. Find the Duplicate Number

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-n','--nums', nargs='+', type=int,
        help="Integer array")
    
    parser.add_argument('-d', '--description', action='store_true',
        help="Show description")
    parser.add_argument('-e', '--example', action='store_true',
        help="Show example")
    
    return parser


class Solution:
    def findDuplicate(self, nums: list) -> int:
        nums.sort()
        for idx, el in enumerate(nums):
            if idx > 0:
                if el == nums[idx - 1]:
                    return el


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each
integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated
number.

You must solve the problem without modifying the array nums and uses
only constant extra space.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0287.py --nums 1 3 4 2 2
    >>> 2

Example 2:
    $ python3 l-0287.py --nums 3 1 3 4 2
    >>> 3
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().findDuplicate(args.nums)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
