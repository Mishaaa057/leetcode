# 2119. A Number After a Double Reversal

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', '--num', type=int, nargs=1,
        help='Integer Num')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        r = int(str(int(str(num)[::-1]))[::-1])
        return r == num


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2119. A Number After a Double Reversal

Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as
the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse
reversed1 to get reversed2. Return true if reversed2 equals num.
Otherwise return false.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2119.py --num 526
    >>> True
{Fore.GREEN}
    Explanation:
        Reverse num to get 625, then reverse 625 to get 526, which
        equals num.
{Fore.RESET}
Example 2:
    $ python l-2119.py --num 1800
    >>> False
{Fore.GREEN}
    Explanation:
        Reverse num to get 81, then reverse 81 to get 18, which does
        not equal num.
{Fore.RESET}
Example 3:
    $ python3 l-2119.py --num 0
    >>> True
{Fore.GREEN}
    Explanation:
        Reverse num to get 0, then reverse 0 to get 0, which equals
        num.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.num:
        result = Solution().isSameAfterReversals(args.num[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
