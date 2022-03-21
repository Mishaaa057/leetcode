# 1374. Generate a String With Characters That Have Odd Counts

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-n', nargs=1, type=int,
        help='Integer N')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            string = ('a' * (n-1)) + 'b'
        
        else:
            string = 'a' * n
        
        return string


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1374. Generate a String With Characters That Have Odd Counts

Given an integer n, return a string with n characters such that each
character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If
there are multiples valid strings, return any of them. 
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''
    
    example = f'''
Example 1:
    $ python3 l-1374.py -n 4
    >>> "pppz"
{Fore.GREEN}
    Explanation:
        "pppz" is a valid string since the character 'p' occurs three
        times and the character 'z' occurs once. Note that there are
        many other valid strings such as "ohhh" and "love".
{Fore.RESET}
Example 2:
    $ python3 l-1374.py -n 2
    >>> "xy"
{Fore.GREEN}
    Explanation:
        "xy" is a valid string since the characters 'x' and 'y' occur
        once. Note that there are many other valid strings such as
        "ag" and "ur".
{Fore.RESET}
Example 3:
    $ python3 l-1374.py -n 7
    >>> "holasss"
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.n:
        result = Solution().generateTheString(args.n[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
