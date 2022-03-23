# 991. Broken Calculator

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-sV', '--startValue', nargs=1, type=int,
        help='Start Value')
    parser.add_argument('-t', '--target', nargs=1, type=int,
        help='Target value')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        counter = 0
        
        while startValue < target:
            counter += 1
            
            if target % 2 == 0:
                target /= 2
            else:
                target += 1
            
        return int(counter + (startValue - target))


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 991. Broken Calculator

There is a broken calculator that has the integer startValue on its
display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number
of operations needed to display target on the calculator.
{Fore.GREEN}
{Fore.RED+('='*70)+Fore.RESET}
    '''
    
    example = f'''
Example 1:
    $ python3 l-0991.py --startValue 2 --target 3
    >>> 2
{Fore.GREEN}
    Explanation:
        Use double operation and then decrement operation [2 -> 4 -> 3].
{Fore.RESET}
Example 2:
    $ python3 l-0991.py --startValue 5 --target 8
    >>> 2
{Fore.GREEN}
    Explanation:
        Use decrement and then double [5 -> 4 -> 8].
{Fore.RESET}
Example 3:
    $ python3 l-0991.py --startValue 3 --target 10
    >>> 3
{Fore.GREEN}
    Explanation:
        Use double, decrement and double [3 -> 6 -> 5 -> 10].
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.startValue and args.target:
        result = Solution().brokenCalc(args.startValue[0], args.target[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()