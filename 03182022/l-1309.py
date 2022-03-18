# 1309. Decrypt String from Alphabet to Integer Mapping

import string
import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', nargs=1, type=str,
        help='String S')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show descripiton')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')

    return parser


class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = string.ascii_lowercase
        
        idx = 0
        res = ''
        
        while idx <= len(s)-1:
            
            el = s[idx]
            
            if idx + 2 <= len(s)-1:
                val = s[idx:][:3]
                if val[-1] == '#':
                    el = val[:2]
                    idx += 2
                    
            if el != '#':
                res += letters[int(el)-1]
            
            idx += 1
        
        return res


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 1309. Decrypt String from Alphabet to Integer Mapping

You are given a string s formed by digits and '#'. We want to map s
to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#')
respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always
exist.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1309.py -s "10#11#12"
    >>> "jkab"
{Fore.GREEN}
    Explanation:
        "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
{Fore.RESET}
Example 2:
    $ python3 l-1309.py -s "1326#"
    >>> "acz"
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().freqAlphabets(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
