# 2129. Capitalize the Title

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-t', '--title', type=str, nargs=1,
        help='Title')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        lst = title.split()
        
        result = ''
        
        for el in lst:
            if len(el) >= 3:
                result += el.title() + ' '
            else:
                result += el.lower() + ' '
        return result[:-1]


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2129. Capitalize the Title

You are given a string title consisting of one or more words
separated by a single space, where each word consists of English
letters. Capitalize the string by changing the capitalization of each
word such that:

If the length of the word is 1 or 2 letters, change all letters to
lowercase.
Otherwise, change the first letter to uppercase and the remaining
letters to lowercase.
Return the capitalized title.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2129.py --title "capiTalIze tHe titLe"
    >>> "Capitalize The Title"
{Fore.GREEN}
    Explanation:
        Since all the words have a length of at least 3, the first
        letter of each word is uppercase, and the remaining letters
        are lowercase.
{Fore.RESET}
Example 2:
    $ python3 l-2129.py --title "First leTTeR of EACH Word"
    >>> "First Letter of Each Word"
    
    Explanation:
        The word "of" has length 2, so it is all lowercase.
        The remaining words have a length of at least 3, so the first
        letter of each remaining word is uppercase, and the remaining
        letters are lowercase.
{Fore.RESET}
Example 3:
    $ python3 l-2129.py --title "i lOve leetcode"
    >>> "i Love Leetcode"
{Fore.GREEN}
    Explanation:
        The word "i" has length 1, so it is lowercase.
        The remaining words have a length of at least 3, so the first
        letter of each remaining word is uppercase, and the remaining
        letters are lowercase.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.title:
        result = Solution().capitalizeTitle(args.title[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()


