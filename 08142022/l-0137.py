# 137. Single Number II
# Medium

import argparse
from colorama import Fore


class Solution:
    def singleNumber(self, nums: list) -> int:
        # Create dictionary
        dct = {}
        
        for el in nums:
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        
        keys = list(dct.keys())
        values = list(dct.values())
        result_idx = values.index(1)

        return keys[result_idx]


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', '--nums', type=int, nargs='+',
        help='Integer array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
    # 137. Single Number II

Given an integer array nums where every element appears three times
except for one, which appears exactly once. Find the single element
and return it.

You must implement a solution with a linear runtime complexity and
use only constant extra space.
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0137.py --nums 2 2 3 2
    >>> 3

Example 2:
    $ python3 l-0137.py --nums 0 1 0 1 0 1 99
    >>> 99
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().singleNumber(args.nums)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
