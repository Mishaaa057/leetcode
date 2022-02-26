# 1078. Occurrences After Bigram

from colorama import Fore
import argparse

def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-t', '--text', type=str, nargs=1,
        help='Integer array')

    parser.add_argument('-f', '--first', type=str, nargs=1,
        help='First')
    
    parser.add_argument('-s', '--second', type=str, nargs=1,
        help='Second')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list:
        lst = text.split(' ')
        
        result = []
        
        for idx, el in enumerate(lst):
            if idx + 2 <= len(lst) - 1:
                if el == first and lst[idx + 1] == second:
                    result.append(lst[idx + 2])
        
        return result


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1078. Occurrences After Bigram

Given two strings first and second, consider occurrences in some text
of the form "first second third", where second comes immediately
after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first
second third".
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1078.py --text "alice is a good girl she is a good student" --first "a" --second "good"
    >>> ["girl","student"]

Example 2:
    $ python3 l-1078.py --text "we will we will rock you" --first "we" --second "will"
    >>> ["we","rock"]
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.text and args.first and args.second:
        result = Solution().findOcurrences(args.text[0], args.first[0], args.second[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
