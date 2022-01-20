# 338. Counting Bits

import argparse 
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', type=int, nargs=1, help='Integer N')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser 


class Solution:
    def countBits(self, n: int) -> list:
        result = []
        
        for i in range(n+1):
            n = str(bin(i))[2:]
            result.append(n.count('1'))
        
        return result


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that
for each i (0 <= i <= n), ans[i] is the number of 1's in the
binary representation of i.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0338.py -n 2
    >>> [0,1,1]
{Fore.GREEN}
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
{Fore.RESET}
Example 2:
    $ python3 l0338.py -n 5
    >>> [0,1,1,2,1,2]
{Fore.GREEN}
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.n:
        result = Solution().countBits(args.n[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()