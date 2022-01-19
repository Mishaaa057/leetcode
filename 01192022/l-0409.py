# 409. Longest Palindrome

import argparse
from ast import arg
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', type=str, nargs=1, help='String')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dct = {}
        for el in s:
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        
        already_noneven = True
        counter = 0

        for el in sorted(dct.values())[::-1]:
            if el % 2 == 0:
                counter += el
            else:
                if already_noneven:
                    counter += el
                    already_noneven = False
                else:
                    counter += el -1
        return counter


def main():
    descr = f'''
{Fore.RED+("-"*70)+Fore.RESET}
{Fore.GREEN}
    # 409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with
those letters.

Letters are case sensitive, for example, "Aa" is not considered a
palindrome here.
{Fore.RESET}
{Fore.RED+("-"*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0409.py -s "abccccdd"
    >>> 7
{Fore.GREEN}
    Explanation:
        One longest palindrome that can be built is "dccaccd", whose
        length is 7.
{Fore.RESET}
Example 2:
    $ python3 l-0409.py -s "a"
    >>> 1

Example 3:
    $ python3 l-0409.py -s "bb"
    >>> 2
    '''

    parser = BuildArgParser(descr)
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