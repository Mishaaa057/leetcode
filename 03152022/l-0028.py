# 28. Implement strStr()

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('--haystack', type=str, nargs=1,
        help='Haystack string')
    parser.add_argument('--needle', type=str, nargs=1,
        help='Needle string')

    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == '':
            return 0
        
        for idx, el in enumerate(haystack):
            n = len(needle)
            
            if idx + n <= len(haystack):
                temp = haystack[idx:idx+n]
                
                if temp == needle:
                    return idx
        
        return -1


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 28. Implement strStr()

Implement strStr.

Return the index of the first occurrence of needle in haystack, or -1
if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great
question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an
empty string. This is consistent to C's strstr() and Java's indexOf().
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''
    
    example = '''
Example 1:
    $ python3 l-0028.py --haystack "hello" --needle "ll"
    >>> 2

Example 2:
    $ python3 l-0028.py --haystack "aaaaa" --needle "bba"
    >>> -1
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.haystack and args.needle:
        result = Solution().strStr(args.haystack[0], args.needle[0])
        print(result)

    elif args.description:
        print(descr)

    elif args.example:
        print(example)

    else:
        parser.print_help()
 

if __name__=="__main__":
    main()
