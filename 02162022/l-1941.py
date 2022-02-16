# 1941. Check if All Characters Have Equal Number of Occurrences

import argparse
from colorama import Fore


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
    def areOccurrencesEqual(self, s: str) -> bool:
        dct = {}
        
        for el in s:
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        
        lst = list(dct.fromkeys(dct.values()))
        
        return len(lst) == 1


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, return true if s is a good string, or false
otherwise.

A string s is good if all the characters that appear in s have the
same number of occurrences (i.e., the same frequency).
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1941.py -s "abacbc"
    >>> True
{Fore.GREEN}
    Explanation:
        The characters that appear in s are 'a', 'b', and 'c'. All
        characters occur 2 times in s.
{Fore.RESET}
Example 2:
    $ python3 l-1941.py -s "aaabb"
    >>> False
{Fore.GREEN}
    Explanation:
        The characters that appear in s are 'a' and 'b'.
    'a' occurs 3 times while 'b' occurs 2 times, which is not the
    same number of times.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().areOccurrencesEqual(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
