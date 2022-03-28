# 747. Largest Number At Least Twice of Others

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
    def dominantIndex(self, nums: list) -> int:
        
        if len(nums) == 1:
            return 0
        
        n_max = max(nums)
        
        for el in nums:
            if el * 2 > n_max and el != n_max:
                return -1
        
        return nums.index(n_max)


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 747. Largest Number At Least Twice of Others

You are given an integer array nums where the largest integer is
unique.

Determine whether the largest element in the array is at least
twice as much as every other number in the array. If it is, return
the index of the largest element, or return -1 otherwise.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0747.py --nums 3 6 1 0
    >>> 1
{Fore.GREEN}
    Explanation:
        6 is the largest integer.
        For every other number in the array x, 6 is at least twice as big as x.
        The index of value 6 is 1, so we return 1.
{Fore.RESET}
Example 2:
    $ python3 l-0747.py --nums 1 2 3 4
    >>> -1
{Fore.GREEN}
    Explanation:
        4 is less than twice the value of 3, so we return -1.
{Fore.RESET}
Example 3:
        $ python3 l-0747.py --nums 1
    >>> 0
{Fore.GREEN}
    Explanation:
        1 is trivially at least twice the value as any other number
        because there are no other numbers.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().dominantIndex(args.nums)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
