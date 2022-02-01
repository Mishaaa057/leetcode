# 151. Reverse Words in a String

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
    def reverseWords(self, s: str) -> str:
        lst = s.split(' ')
        lst = lst[::-1]
        
        result = ''
        for el in lst:
            if el != '':
                result += el + ' '
                
        return result[:-1]


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in
s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a
single space.

Note that s may contain leading or trailing spaces or multiple spaces
between two words. The returned string should only have a single
space separating the words. Do not include any extra spaces.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0151.py -s "the sky is blue"
    >>> "blue is sky the"

Example 2:
    $ python3 l-0151.py -s "  hello world  "
    >>> "world hello"
{Fore.GREEN}
    Explanation:
        Your reversed string should not contain
        leading or trailing spaces.
{Fore.RESET}
Example 3:
    $ python3 l-0151.py -s "a good   example"
    >>> "example good a"
{Fore.GREEN}
    Explanation:
        You need to reduce multiple spaces between two words to a
        single space in the reversed string.
 {Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.string:
        result = Solution().reverseWords(args.string[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
