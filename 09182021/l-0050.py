# 50. Pow(x, n)

from colorama import Fore
import argparse


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-x', nargs=1, type=int, help='x')
    parser.add_argument('-n', nargs=1, type=int, help='n')
    parser.add_argument('--description', '-d', action='store_true',
        help='Show description')
    parser.add_argument('--example', '-e', action='store_true',
        help='Show example')

    return parser 


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


def Main():
    descr = f'''
{Fore.RED}================================================={Fore.RESET}
    {Fore.GREEN}# 50. Pow(x, n)

Implement pow(x, n), which calculates x raised 
to the power n (i.e., xn).{Fore.RESET}
{Fore.RED}================================================={Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0050.py -x 2.00000 -n 10
    >>> 1024.00000

Example 2:

    $ python3 l-0050.py -x 2.10000 -n 3
    >>> 9.26100

Example 3:
    $ python3 l-0050.py -x 2.00000 -n -2
    >>> 0.25000
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.x and args.n:
        result = Solution().myPow(args.x[0], args.n[0])
        print(result)

    elif args.description:
        print(descr)

    elif args.example:
        print(example)

    else:
        parser.print_help()


if __name__=='__main__':
    Main()