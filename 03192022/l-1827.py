# 1827. Minimum Operations to Make the Array Increasing

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', '--nums', nargs='+', type=int,
        help='Integer array')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def minOperations(self, nums: list) -> int:
        """
        
        input = 1 5 2 4 1
        
        1 5 6(2+4) 7(4+3) 8(1+8)
                
        """
        
        counter = 0
        
        for idx, el in enumerate(nums):
            if idx < len(nums)-1:
                next = nums[idx+1]
                if next <= el:
                    n = el + 1 - next
                    counter += n
                    nums[idx+1] = n+next
        
        return counter


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 1827. Minimum Operations to Make the Array Increasing

You are given an integer array nums (0-indexed). In one operation,
you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1]
to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly
increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0
<= i < nums.length - 1. An array of length 1 is trivially strictly
increasing.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1827.py --nums 1 1 1
    >>> 3
{Fore.GREEN}
    Explanation: You can do the following operations:
        1) Increment nums[2], so nums becomes [1,1,2].
        2) Increment nums[1], so nums becomes [1,2,2].
        3) Increment nums[2], so nums becomes [1,2,3].
{Fore.RESET}
Example 2:
    $ python3 l-1827.py --nums 1 5 2 4 1
    >>> 14

Example 3:
    $ python3 l-1827.py --nums 8
    >>> 0
    '''
    
    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().minOperations(args.nums)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
