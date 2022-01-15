# 1523. Count Odd Numbers in an Interval Range

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('--low', type=int, nargs=1, help='Non-negative integer Low')
    parser.add_argument('--high', type=int, nargs=1, help='Non-negative integer High')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser 


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        elif low % 2 != 0 and high % 2 != 0:
            return (high - low) // 2 + 1
        else:
            return (high - low) // 2 + 1


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
# 1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd
numbers between low and high (inclusive).
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1525.py --low 3 --high 7
    >>> 3
{Fore.GREEN}
    Explanation:
        The odd numbers between 3 and 7 are [3,5,7].
{Fore.RESET}
Example 2:
    $ python3 l-1525.py --low 8 --high 10
    >>> 1
{Fore.GREEN}
    Explanation:
        The odd numbers between 8 and 10 are [9].
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.low and args.high:
        result = Solution().countOdds(args.low[0], args.high[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
