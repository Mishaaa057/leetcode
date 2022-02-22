# 171. Excel Sheet Column Number

import argparse
from colorama import Fore
import string


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-cT', '--columnTitle', type=str, nargs=1,
        help='Column Title')

    parser.add_argument('-d', '--description', action='store_true',
        help='Sow description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Sow example')
    
    return parser


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = list(string.ascii_uppercase)
        
        s = columnTitle[::-1]
        
        result = 0
        for idx, el in enumerate(s):
            
            if idx == 0:
                n = 1
            else:
                n = 26**idx
                
            result += (letters.index(el) + 1) * n
        
        return result
        


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appear
in an Excel sheet, return its corresponding column number.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0171.py --columnTitle "A"
    >>> 1

Example 2:
    $ python3 l-0171.py --columnTitle "AB"
    >>> 28

Example 3:
    $ python3 l-0171.py --columnTitle "ZY"
    >>> 701
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.columnTitle:
        result = Solution().titleToNumber(args.columnTitle[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
