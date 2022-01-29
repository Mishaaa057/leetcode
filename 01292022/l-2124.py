# 2124. Check if All A's Appears Before All B's

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', '--string', type=str, nargs=1,
        help='String')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def checkString(self, s: str) -> bool:
        a = []
        b = []
        for idx, el in enumerate(s):
            if el == 'a':
                a.append(idx)
            elif el == 'b':
                b.append(idx)

        if len(a) == 0 or len(b) == 0:
            return True
        
        n = min(b)

        for el in a:
            if el > n:
                return False
        return True


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2124. Check if All A's Appears Before All B's

Given a string s consisting of only the characters 'a' and 'b',
return true if every 'a' appears before every 'b' in the string.
Otherwise, return false.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2124.py -s "aaabbb"
    >>> True
{Fore.GREEN}
    Explanation:
        The 'a's are at indices 0, 1, and 2, while the 'b's are at
        indices 3, 4, and 5.
        Hence, every 'a' appears before every 'b' and we return true.
{Fore.RESET}
Example 2:
    $ python3 l-2124.py -s "abab"
    >>> False
{Fore.GREEN}
    Explanation:
        There is an 'a' at index 2 and a 'b' at index 1.
        Hence, not every 'a' appears before every 'b' and we return
        false.
{Fore.RESET}
Example 3:
    $ python3 l-2124.py -s "bbb"
    >>> True
{Fore.GREEN}
    Explanation:
        There are no 'a's, hence, every 'a' appears before every 'b'
        and we return true.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.string:
        result = Solution().checkString(args.string[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
