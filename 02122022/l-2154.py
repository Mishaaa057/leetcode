# 2154. Keep Multiplying Found Values by Two

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', '--nums', type=int, nargs='+',
        help='Integer Array')
    parser.add_argument('-o', '--original', type=int, nargs=1,
        help='Integer Original')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def findFinalValue(self, nums: list, original: int) -> int:
        while True:
            if original in nums:
                original = original * 2
            else:
                return original


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2154. Keep Multiplying Found Values by Two

You are given an array of integers nums. You are also given an
integer original which is the first number that needs to be
searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original
= 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding
the number.
Return the final value of original.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''
    
    example = f'''
Example 1:
    $ python3 l-2154.py --nums 5 3 6 1 12 --original 3
    >>> 24
{Fore.GREEN}
    Explanation: 
        - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
        - 6 is found in nums. 6 is multiplied by 2 to obtain 12.
        - 12 is found in nums. 12 is multiplied by 2 to obtain 24.
        - 24 is not found in nums. Thus, 24 is returned.
{Fore.RESET}
Example 2:
    $ python3 l-2154.py --nums 2 7 9 --original 4
    >>> 4
{Fore.GREEN}
    Explanation:
        - 4 is not found in nums. Thus, 4 is returned.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums and args.original:
        result = Solution().findFinalValue(args.nums, args.original[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
