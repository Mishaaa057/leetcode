# 1287. Element Appearing More Than 25% In Sorted Array

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
    def findSpecialInteger(self, arr: list) -> int:
        dct = {}
        
        for el in arr:
            el = str(el)
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        
        ln = len(arr)
        for key in dct:
            n = (dct[key] * 100) / ln
            if n > 25:
                return int(key)


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is
exactly one integer in the array that occurs more than 25% of the
time, return that integer.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-1287.py --arr 1 2 2 6 6 6 6 7 10
    >>> 6

Example 2:
    $ python3 l-1287.py --arr 1 1
    >>> 1
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.arr:
        result = Solution().findSpecialInteger(args.arr)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
