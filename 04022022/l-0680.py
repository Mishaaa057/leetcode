# 680. Valid Palindrome II

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', type=str, nargs=1,
        help='String s')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check(s):
            return s == s[::-1]
        
        if check(s):
            
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            
            if s[i] != s[j]:
                s1 = s[i+1:j+1]
                s2 = s[i:j]
                return check(s1) or check(s2)
            
            i += 1
            j -= 1


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after
deleting at most one character from it.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f"""
Example 1:
    $ python3 l-0680.py -s "aba"
    >>> True

Example 2:
    $ python3 l-0680.py -s "abca"
    >>> True
{Fore.GREEN}
    Explanation:
        You could delete the character 'c'.
{Fore.RESET}
Example 3:
    $ python3 l-0680.py -s "abc"
    >>> False
    """

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().validPalindrome(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)

    else:
        parser.print_help()


if __name__=="__main__":
    main()
