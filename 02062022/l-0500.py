# 500. Keyboard Row

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-w', '--words', type=str, nargs='+',
        help='Words array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def findWords(self, words: list) -> list:
        top = 'qwertyuiop'
        mid = 'asdfghjkl'
        down = 'zxcvbnm'
        
        results = []
        
        for org_word in words:
            word = org_word.lower()
            char = word[0]
            
            if char in top:
                row = top
            elif char in mid:
                row = mid
            else:
                row = down
            
            is_in = True
            
            for el in word:
                if el not in row:
                    is_in = False
            
            if is_in:
                results.append(org_word)
        
        return results


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 500. Keyboard Row

Given an array of strings words, return the words that can be typed
using letters of the alphabet on only one row of American keyboard
like the image below.

In the American keyboard:
    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0500.py --words "Hello" "Alaska" "Dad" "Peace"
    >>> ["Alaska","Dad"]

Example 2:
    $ python3 l-0500.py --words "omk"
    >>> []

Example 3:
    $ python3 l-0500.py --words "adsdf" "sfd"
    >>> ["adsdf","sfd"]
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.words:
        result = Solution().findWords(args.words)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
