# 1518. Water Bottles

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-nb', '--numBottles', type=int, nargs=1,
        help='Number of bottles')
    parser.add_argument('-ne', '--numExchange', type=int, nargs=1,
        help='Number of exchange')

    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counter = numBottles
        while True:

            if numBottles >= numExchange:
                n = numBottles // numExchange
                counter += n
                
                numBottles = n + numBottles % numExchange    

            else:
                break

        return counter


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1518. Water Bottles

There are numBottles water bottles that are initially full of water.
You can exchange numExchange empty water bottles from the market with
one full water bottle.

The operation of drinking a full water bottle turns it into an empty
bottle.

Given the two integers numBottles and numExchange, return the maximum
number of water bottles you can drink.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1518.py --numBottles 9 --numExchange 3
    >>> 13
{Fore.GREEN}
    Explanation:
        You can exchange 3 empty bottles to get 1 full water bottle.
        Number of water bottles you can drink: 9 + 3 + 1 = 13.
{Fore.RESET}
Example 2:
    $ python3 l-1518.py --numBottles 15 --numExchange 4
    >>> 19
{Fore.GREEN}
    Explanation:
        You can exchange 4 empty bottles to get 1 full water bottle. 
        Number of water bottles you can drink: 15 + 3 + 1 = 19.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.numBottles and args.numExchange:
        result = Solution().numWaterBottles(args.numBottles[0], args.numExchange[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
    
    