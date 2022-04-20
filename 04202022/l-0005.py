# 5. Longest Palindromic Substring

import argparse
from tkinter import E
from colorama import Fore


def BuildArgParse(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', type=str, nargs=1,
        help='String S')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ''
        resLen = 0
        
        for i in range(len(s)):
            # odd lenght
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                l -= 1
                r += 1
            
            #even lenght
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                l -= 1
                r += 1
        
        return res


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''
    
    example = f'''
Example 1:
    $ python3 l-0005.py -s "babad"
    >>> "bab"
{Fore.GREEN}
    Explanation:
        "aba" is also a valid answer.
{Fore.RESET}
Example 2:
    $ python3 l-0005.py -s "cbbd"
    >>> "bb"
    '''

    parser = BuildArgParse(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().longestPalindrome(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()

if __name__=="__main__":
    main()
