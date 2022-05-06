# 2239. Find Closest Number to Zero

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-n', '--nums', nargs='+', type=int,
        help='Integer Array')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def findClosestNumber(self, nums: list) -> int:
        lst1 = []
        lst2 = []
        
        for el in nums:
            if el < 0:
                lst1.append(el)
            elif el > 0:
                lst2.append(el)
            else:
                return 0
        
        n1 = float('-inf')
        n2 = float('inf')
        
        if lst1:
            n1 = max(lst1)
        
        if lst2:
            n2 = min(lst2)
        
        if abs(n1) < n2:
            return n1
        else:
            return n2


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2239. Find Closest Number to Zero

Given an integer array nums of size n, return the number with the
value closest to 0 in nums. If there are multiple answers, return the
number with the largest value.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2239.py --nums -4 -2 1 4 8
    >>> 1
{Fore.GREEN}
    Explanation:
        The distance from -4 to 0 is |-4| = 4.
        The distance from -2 to 0 is |-2| = 2.
        The distance from 1 to 0 is |1| = 1.
        The distance from 4 to 0 is |4| = 4.
        The distance from 8 to 0 is |8| = 8.
        Thus, the closest number to 0 in the array is 1.
{Fore.RESET}
Example 2:
    $ python3 l-2239.py --nums 2 -1 1
    >>> 1
{Fore.GREEN}
    Explanation:
        1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
{Fore.RESET}
    '''
    
    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().findClosestNumber(args.nums)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
