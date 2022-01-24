# 520. Detect Capital

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-w', '--word', type=str, nargs=1,
        help='Word')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if all chars uppercase
        if word == word.upper():
            return True
        # Check if all chars without first are lowercase
        # First char no difference lowercase or upercase
        else:
            return word[1:] == word[1:].lower()


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 520. Detect Capital

We define the usage of capitals in a word to be right when one of the
following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is
right.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0520.py --word "USA"
    >>> True

Example 2:
    $ python3 l-0520.py --word "FlaG"
    >>> False
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.word:
        result = Solution().detectCapitalUse(args.word[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
    