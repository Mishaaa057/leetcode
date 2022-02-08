# 1207. Unique Number of Occurrences

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-a', '--arr', type=int, nargs='+',
        help='Integer array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        dct = {}
        
        for el in arr:
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
                
        values = list(dct.values())
        for el in values:
            if values.count(el) != 1:
                return False
        return True


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of
occurrences of each value in the array is unique, or false otherwise.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1207.py --arr 1 2 2 1 1 3
    >>> True
{Fore.GREEN}
    Explanation:
        The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
        values have the same number of occurrences.
{Fore.RESET}
Example 2:
    $ python3 l-1207.py --arr 1 2
    >>> False

Example 3:
    $ python3 l-1207.py --arr -3 0 1 -3 1 1 1 -3 10 0
    >>> True
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.arr:
        result = Solution().uniqueOccurrences(args.arr)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
