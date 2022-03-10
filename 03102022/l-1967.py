# 1967. Number of Strings That Appear as Substrings in Word

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-p', '--patterns', type=str, nargs='+',
        help='Array of patterns')
    parser.add_argument('-w', '--word', type=str, nargs=1,
        help='Word')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def numOfStrings(self, patterns: list, word: str) -> int:
        counter = 0
        for el in patterns:
            if el in word:
                counter += 1
        
        return counter
    

def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 1967. Number of Strings That Appear as Substrings in Word

Given an array of strings patterns and a string word, return the
number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1967.py --patterns "a" "abc" "bc" "d" --word "abc"
    >>> 3
{Fore.GREEN}
    Explanation:
    - "a" appears as a substring in "abc".
    - "abc" appears as a substring in "abc".
    - "bc" appears as a substring in "abc".
    - "d" does not appear as a substring in "abc".
    3 of the strings in patterns appear as a substring in word.
{Fore.RESET}
Example 2:
    $ python3 l-1967.py --patterns "a" "b" "c" --word "aaaaabbbbb"
    >>> 2
{Fore.GREEN}
    Explanation:
    - "a" appears as a substring in "aaaaabbbbb".
    - "b" appears as a substring in "aaaaabbbbb".
    - "c" does not appear as a substring in "aaaaabbbbb".
    2 of the strings in patterns appear as a substring in word.
{Fore.RESET}
Example 3:
    $ python3 l-1967.py --patterns "a" "a" "a" --word "ab"
    >>> 3
{Fore.GREEN}
    Explanation:
    Each of the patterns appears as a substring in word "ab".
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.patterns and args.word:
        result = Solution().numOfStrings(args.patterns, args.word[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
