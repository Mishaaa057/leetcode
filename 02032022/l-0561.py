# 561. Array Partition I

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
    def arrayPairSum(self, nums: list) -> int:
        lst = sorted(nums)
        
        result = 0
        for _ in range(len(lst)//2):
            pair = lst[:2]
            lst = lst[2:]
            result += min(pair)
        
        return result
            

def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 561. Array Partition I

Given an integer array nums of 2n integers, group these integers into
n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of
min(ai, bi) for all i is maximized. Return the maximized sum.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0561.py --nums 1 4 3 2
    >>> 4
{Fore.GREEN}
    Explanation:
        All possible pairings (ignoring the ordering of elements) are:
        1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
        2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
        3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
        So the maximum possible sum is 4.
{Fore.RESET}
Example 2:
    $ python3 l-0561.py --nums 6 2 6 5 1 2
    >>> 9
{Fore.GREEN}
    Explanation:
        The optimal pairing is (2, 1), (2, 5), (6, 6).
        min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().arrayPairSum(args.nums)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
