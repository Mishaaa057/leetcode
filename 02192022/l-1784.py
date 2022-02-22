# 1784. Check if Binary String Has at Most One Segment of Ones

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-s', type=str, nargs=1,
        help='Binary string S')

    parser.add_argument('-d', '--description', action='store_true',
        help='Sow description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Sow example')
    
    return parser


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        lst = s.split('0')
        
        counter = 0
        for el in lst:
            if '1' in el:
                counter += 1
                if counter > 1:
                    return False
        
        return True


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1784. Check if Binary String Has at Most One Segment of Ones

Given a binary string s without leading zeros, return true if s
contains at most one contiguous segment of ones. Otherwise,
return false.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1784.py -s "1001"
    >>> False
{Fore.GREEN}
    Explanation:
        The ones do not form a contiguous segment.
{Fore.RESET}
Example 2:
    $ python3 l-1784.py -s "110"
    >>> True
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().checkOnesSegment(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
