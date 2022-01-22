# 1046. Last Stone Weight

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', '--stones', type=int, nargs='+',
        help='Integers stones where stones[i] is the weight')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')

    return parser


class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        
        while len(stones) > 1:
            x_stone = max(stones)
            stones.remove(x_stone)
            
            y_stone = max(stones)
            stones.remove(y_stone)
            
            if x_stone != y_stone:
                stones.append(abs(x_stone - y_stone))
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1046. Last Stone Weight

You are given an array of integers stones where stones[i] is the
weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the
heaviest two stones and smash them together. Suppose the heaviest two
stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of
weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are
no stones left, return 0.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1046.py --stones 2 7 4 1 8 1
    >>> 1
{Fore.GREEN}
    Explanation: 
        We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
        we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
        we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
        we combine 1 and 1 to get 0 so the array converts to [1] then that's
        the value of the last stone.
{Fore.RESET}
Example 2:
    $ python3 l-1046.py --stones 1
    >>> 1    
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.stones:
        result = Solution().lastStoneWeight(args.stones)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
