# 1935. Maximum Number of Words You Can Type

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-t', '--text', type=str, nargs=1,
        help='Text string')
    parser.add_argument('-bL', '--brokenLetters', type=str, nargs=1,
        help='Broken Letters string')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        counter = 0
        
        for word in text.split(' '):
            add = True
            for el in word:
                
                if el in brokenLetters:
                    add = False
                    break
                
            if add:
                counter += 1
        
        return counter


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1935. Maximum Number of Words You Can Type

There is a malfunctioning keyboard where some letter keys do not
work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading
or trailing spaces) and a string brokenLetters of all distinct letter
keys that are broken, return the number of words in text you can
fully type using this keyboard.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1935.py --text "hello world" --brokenLetters "ad"
    >>> 1
{Fore.GREEN}
    Explanation:
        We cannot type "world" because the 'd' key is broken.
{Fore.RESET}
Example 2:
    $ python3 l-1935.py --text "leet code" --brokenLetters "lt"
    >>> 1
{Fore.GREEN}
    Explanation:
        We cannot type "leet" because the 'l' and 't' keys are broken.
{Fore.RESET}
Example 3:
    $ python3 l-1935.py --text "leet code" --brokenLetters "e"
    >>> 0
{Fore.GREEN}
    Explanation:
        We cannot type either word because the 'e' key is broken.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.text and args.brokenLetters:
        result = Solution().canBeTypedWords(args.text[0], args.brokenLetters[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
