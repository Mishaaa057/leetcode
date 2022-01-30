# 724. Find Pivot Index

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', '--nums', type=int, nargs='+',
        help='Integer array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def pivotIndex(self, nums: list) -> int:
        for idx, el in enumerate(nums):
            left = sum(nums[:idx])
            right = sum(nums[idx+1:])
            
            if left == right:
                return idx
        return -1


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this
array.

The pivot index is the index where the sum of all the numbers
strictly to the left of the index is equal to the sum of all the
numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is
0 because there are no elements to the left. This also applies to
the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0724.py --nums 1 7 3 6 5 6
    >>> 3
{Fore.GREEN}
    Explanation:
        The pivot index is 3.
        Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
        Right sum = nums[4] + nums[5] = 5 + 6 = 11
{Fore.RESET}
Example 2:
    $ python3 l-0724.py --nums 1 2 3
    >>> -1
{Fore.GREEN}
    Explanation:
        There is no index that satisfies the conditions in the problem statement.
{Fore.RESET}
Example 3:
    $ python3 l-0724.py --nums 2 1 -1
    >>> 0
{Fore.GREEN}
    Explanation:
        The pivot index is 0.
        Left sum = 0 (no elements to the left of index 0)
        Right sum = nums[1] + nums[2] = 1 + -1 = 0
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().pivotIndex(args.nums)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
