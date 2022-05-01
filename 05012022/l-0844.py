# 844. Backspace String Compare

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-s', type=str, nargs=1, help='String S')
    parser.add_argument('-t', type=str, nargs=1, help='String T')

    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show exampl')
    
    return parser


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        while '#' in s:
            idx = s.index('#')
            s.pop(idx)
            if idx != 0:
                s.pop(idx-1)
        
        while '#' in t:
            idx = t.index('#')
            t.pop(idx)
            if idx != 0:
                t.pop(idx-1)
            
        return s == t


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 844. Backspace String Compare

Given two strings s and t, return true if they are equal when both
are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue
empty.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0844.py -s "ab#c" -t "ad#c"
    >>> True
{Fore.GREEN}
    Explanation:
        Both s and t become "ac".
{Fore.RESET}
Example 2:
    $ python3 l-0844.py -s "ab##" -t "c#d#"
    >>> True
{Fore.GREEN}
    Explanation:
        Both s and t become "".
{Fore.RESET}
Example 3:
    $ python3 l-0844.py -s "a#c" -t "b"
    >>> False
{Fore.GREEN}
    Explanation:
        s becomes "c" while t becomes "b".
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s and args.t:
        result = Solution().backspaceCompare(args.s[0], args.t[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
