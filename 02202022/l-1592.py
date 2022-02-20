# 1592. Rearrange Spaces Between Words

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-t', '--text', type=str, nargs=1,
        help='Text string')

    parser.add_argument('-d', '--description', action='store_true',
        help='Sow description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Sow example')
    
    return parser


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces_count = text.count(' ')
        
        lst = text.split(' ')
        lst = [el for el in lst if el != '']
        
        words_count = len(lst)
        
        if len(text) == 1:
            return text
        
        if words_count > 1:
            n = spaces_count // (words_count - 1)
            n2 = spaces_count % (words_count - 1)
        else:
            n = 1
            n2 = spaces_count
        
        
        result = ''
        
        for idx, el in enumerate(lst):
            if idx < len(lst) - 1:
                result += el + (' '*n)
            else:
                result += el + (' '*n2)
        
        return result
        


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1592. Rearrange Spaces Between Words

You are given a string text of words that are placed among some
number of spaces. Each word consists of one or more lowercase English
letters and are separated by at least one space. It's guaranteed that
text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces
between every pair of adjacent words and that number is maximized. If
you cannot redistribute all the spaces equally, place the extra
spaces at the end, meaning the returned string should be the same
length as text.

Return the string after rearranging the spaces.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1592.py --text "  this   is  a sentence "
    >>> "this   is   a   sentence"
{Fore.GREEN}
    Explanation:
        There are a total of 9 spaces and 4 words. We can evenly
        divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
{Fore.RESET}
Example 2:
    $ python3 l-1592.py --text " practice   makes   perfect"
    >>> "practice   makes   perfect "
{Fore.GREEN}
    Explanation:
        There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces
        plus 1 extra space. We place this extra space at the end of the string.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.text:
        result = Solution().reorderSpaces(args.text[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
