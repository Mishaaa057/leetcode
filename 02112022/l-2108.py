# 2108. Find First Palindromic String in the Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-w', '--words', type=str, nargs='+',
        help='Words Array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')    
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')    
    
    return parser


class Solution:
    def firstPalindrome(self, words: list) -> str:
        for el in words:
            if el == el[::-1]:
                return el
        return ''


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2108. Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string
in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2108.py --words "abc" "car" "ada" "racecar" "cool"
    >>> "ada"
{Fore.GREEN}
    Explanation:
        The first string that is palindromic is "ada".
        Note that "racecar" is also palindromic, but it is not the first.
{Fore.RESET}
Example 2:
    $ python3 l-2108.py --words "notapalindrome" "racecar"
    >>> "racecar"
{Fore.GREEN}
    Explanation:
        The first and only string that is palindromic is "racecar".
{Fore.RESET}
Example 3:
    $ python3 l-2108.py --words "def" "ghi"
    >>> ""
{Fore.GREEN}
    Explanation:
        There are no palindromic strings, so the empty string is returned.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.words:
        result = Solution().firstPalindrome(args.words)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
