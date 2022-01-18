# 605. Can Place Flowers

import argparse
from colorama import Fore

def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-fb', '--flowerbed', type=int, nargs='+',
        help='Integer array Flowerbed')
    parser.add_argument('-n', type=int, nargs=1, help='Integer N')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            if n == 1:
                return True
        
        lst = []
        end = len(flowerbed) - 1
        
        for idx, el in enumerate(flowerbed):
            if el == 0:
                before = idx - 1
                after = idx + 1
                
                if before >= 0 and after <= end:
                    el_b = flowerbed[before]
                    el_a = flowerbed[after]
                    
                    if el_b != 1 and el_a != 1:
                        if n != 0:
                            n -= 1
                            flowerbed[idx] = 1
                
                # If first el = 0
                elif idx == 0 and after <= end:
                    if flowerbed[after] == 0:
                        n -= 1
                        flowerbed[idx] = 1
                
                # If last el = 0
                elif idx == end and before >= 0:
                    if flowerbed[before] == 0:
                        n -= 1
                        flowerbed[idx] = 1
                
            if n <= 0:
                return True
        return False


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and
some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0
means empty and 1 means not empty, and an integer n, return if n new
flowers can be planted in the flowerbed without violating the
no-adjacent-flowers rule.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''
    
    example = '''
Example 1:
    $ python3 l-0605.py --flowerbed 1 0 0 0 1 -n 1
    >>> True

Example 2:
    $ python3 l-0605.py --flowerbed  1 0 0 0 1 -n 2
    >>> False
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.flowerbed and args.n:
        result = Solution().canPlaceFlowers(args.flowerbed, args.n[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
