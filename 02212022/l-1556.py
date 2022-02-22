# 1556. Thousand Separator

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', type=int, nargs=1,
        help='Integer N')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)[::-1]
        
        result = ''
        n = 0
        for el in s:
            if n <2:
                n += 1
                result += el
            else:
                n = 0
                result += el + '.'
        result = result[::-1]
        
        if result[0] == '.':
            result = result[1:]
        
        return result


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1556. Thousand Separator

Given an integer n, add a dot (".") as the thousands separator and
return it in string format.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1556.py -n 987
    >>> "987"

Example 2:
    $ python3 l-1556.py -n 1234
    >>> "1.234"
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.n:
        result = Solution().thousandSeparator(args.n[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)

    else:
        parser.print_help()


if __name__=="__main__":
    main()
