# 392. Is Subsequence

import argparse
from colorama import Fore

def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-s', type=str, nargs=1, help='String s')
    parser.add_argument('-t', type=str, nargs=1, help='String t')


    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        
        t = list(t)
        indexes = []
        for el in s:
            if el not in t:
                return False
            else:
                while el in t:
                    idx = t.index(el)
                    if indexes:
                        last_idx = indexes[len(indexes) - 1]
                    else:
                        last_idx = -1
                        
                    if idx > last_idx:
                        indexes.append(idx)
                        t[idx] = '-'
                        break
                    else:
                        t[idx] = '-'
                    if el not in t:
                        return False
                        
        return True
        

def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or
false otherwise.

A subsequence of a string is a new string that is formed from the
original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is
not).
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0392.py -s "abc" -t "ahbgdc"
    >>> True

Example 2:
    $ python3 l-0392.py -s "axc" -t "ahbgdc"
    >>> False
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s and args.t:
        result = Solution().isSubsequence(args.s[0], args.t[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
