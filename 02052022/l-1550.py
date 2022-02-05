# 1550. Three Consecutive Odds

import argparse
from colorama import Fore

from pandas import describe_option
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
    def threeConsecutiveOdds(self, arr: list) -> bool:
        for idx, el in enumerate(arr):
            if idx + 3 <= len(arr):
                lst = arr[idx:]
                lst = lst[:3]
                is_odd = True
                for el2 in lst:
                    if el2 % 2 == 0:
                        is_odd = False
                        break
                if is_odd:
                    return True
        return False


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1550. Three Consecutive Odds

Given an integer array arr, return true if there are three
consecutive odd numbers in the array. Otherwise, return false.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1550.py --arr 2 6 4 1
    >>> False
{Fore.GREEN}
    Explanation:
        There are no three consecutive odds.
{Fore.RESET}
Example 2:
    $ python3 l-1550.py --arr 1 2 34 3 4 5 7 23 12
    >>> True
{Fore.GREEN}
    Explanation:
    [5,7,23] are three consecutive odds.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.arr:
        result = Solution().threeConsecutiveOdds(args.arr)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
