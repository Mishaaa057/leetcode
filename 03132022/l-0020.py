# 20. Valid Parentheses

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', type=str, nargs=1,
        help='String s')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            '(':')',
            '[':']',
            '{':'}'
        }
        
        lst = list(s)
        
        while True:
            rep = False
            for idx, el in enumerate(lst):
                if el in dct:
                    if idx + 1 <= len(lst)-1:
                        next_el  = lst[idx+1]
                        if next_el == dct[el]:
                            lst.pop(idx+1)
                            lst.pop(idx)
                            
                            rep = True

                            if len(lst) == 0:
                                return True
                            
            if rep:
                continue
            return False


def main():
    descr = '''
    # 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
    '''

    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
{descr}
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0020.py -s "()"
    >>> True

Example 2:
    $ python3 l-0020.py -s "()[]{}"
    >>> True

Example 3:
    $ python3 l-0020.py -s "(]"
    >>> False
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().isValid(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
    