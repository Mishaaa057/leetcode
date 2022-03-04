# 1800. Maximum Ascending Subarray Sum

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('--nums', type=int, nargs='+',
        help='Integer array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def maxAscendingSum(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        
        results = []
        for idx1, el1 in enumerate(nums):
            temp = [el1]
            for idx2, el2 in enumerate(nums[idx1+1:]):
                idx2 = idx2 + idx1 + 1
                
                if temp[len(temp)-1] < el2:
                    temp.append(el2)
                else:
                    results.append(sum(temp))
                    break

                if idx2 == len(nums) - 1:
                    results.append(sum(temp))
        
        return max(results)
                    


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1800. Maximum Ascending Subarray Sum

Given an array of positive integers nums, return the maximum possible
sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an
array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for
all i where l <= i < r, numsi < numsi+1. Note that a subarray of size
1 is ascending.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1800.py --nums 10 20 30 5 10 50
    >>> 65
{Fore.GREEN}
    Explanation:
        [5,10,50] is the ascending subarray with the maximum sum of 65.
{Fore.RESET}
Example 2:
    $ python3 l-1800.py --nums 10 20 30 40 50
    >>> 150
{Fore.GREEN}
    Explanation:
        [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
{Fore.RESET}
Example 3:
    $ python3 l-1800.py --nums 12 17 15 13 10 11 12
    >>> 33
{Fore.GREEN}
    Explanation:
        [10,11,12] is the ascending subarray with the maximum sum of 33.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().maxAscendingSum(args.nums)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
