# 1844. Replace All Digits with Characters

import argparse
from colorama import Fore
import string


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-s', type=str, nargs=1,
        help='String S')

    parser.add_argument('-d', '--description', action='store_true',
        help='Sow description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Sow example')
    
    return parser


class Solution:
    def replaceDigits(self, s: str) -> str:
        letters = list(string.ascii_lowercase)
        
        result = ''
        
        for idx, el in enumerate(s):
            if el.isdigit():
                i = letters.index(s[idx - 1])
                n = i + int(el)
                result += letters[n]
                
            else:
                result += el
        
        return result


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1844. Replace All Digits with Characters

You are given a 0-indexed string s that has lowercase English letters
in its even indices and digits in its odd indices.

There is a function shift(c, x), where c is a character and x is a
digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with
shift(s[i-1], s[i]).

Return s after replacing all digits. It is guaranteed that
shift(s[i-1], s[i]) will never exceed 'z'.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1844.py -s "a1c1e1"
    >>> "abcdef"
{Fore.GREEN}
    Explanation:
        The digits are replaced as follows:
            - s[1] -> shift('a',1) = 'b'
            - s[3] -> shift('c',1) = 'd'
            - s[5] -> shift('e',1) = 'f'
{Fore.RESET}
Example 2:
    $ python3 l-1844.py -s "a1b2c3d4e"
    >>> "abbdcfdhe"
{Fore.GREEN}
    Explanation:
        The digits are replaced as follows:
            - s[1] -> shift('a',1) = 'b'
            - s[3] -> shift('b',2) = 'd'
            - s[5] -> shift('c',3) = 'f'
            - s[7] -> shift('d',4) = 'h'
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().replaceDigits(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
