# 905. Sort Array By Parity

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('--nums', type=int, nargs='+',
        help='Integer array')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def sortArrayByParity(self, nums: list) -> int:
        odd = []
        even = []
        
        for el in nums:
            if el % 2 == 0:
                even.append(el)
            else:
                odd.append(el)
        
        return even + odd


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 905. Sort Array By Parity

Given an integer array nums, move all the even integers at the
beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0905.py --nums 3 1 2 4
    >>> [2,4,3,1]
{Fore.GREEN}
    Explanation:
        The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be
        accepted.
{Fore.RESET}
Example 2:
    $ python3 l-0905.py --nums 0
    >>> [0]
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().sortArrayByParity(args.nums)
        print(result)

    elif args.description:
        print(descr)

    elif args.example:
        print(example)

    else:
        parser.print_help()


if __name__=="__main__":
    main()
