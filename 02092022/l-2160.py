# 2160. Minimum Sum of Four Digit Number After Splitting Digits

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
    def minimumSum(self, num: int) -> int:
        lst = sorted(str(num))
        
        a = int(lst[0] + lst[2])
        b = int(lst[1] + lst[3])
        
        return a + b


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2160. Minimum Sum of Four Digit Number After Splitting Digits

You are given a positive integer num consisting of exactly four
digits. Split num into two new integers new1 and new2 by using the
digits found in num. Leading zeros are allowed in new1 and new2, and
all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two
2's, one 9 and one 3. Some of the possible pairs [new1, new2] are
[22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2160.py --num 2932
    >>> 52
{Fore.GREEN}
    Explanation:
        Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
        The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
{Fore.RESET}
Example 2:
    $ python3 l-2160.py --num 4009
    >>> 13
{Fore.GREEN}
    Explanation:
        Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
        The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
{Fore.RESET}    
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.num:
        result = Solution().minimumSum(args.num[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)

    else:
        parser.print_help()


if __name__=="__main__":
    main()
