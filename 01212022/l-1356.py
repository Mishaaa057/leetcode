# 1356. Sort Integers by The Number of 1 Bits

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-a', '--arr', type=int, nargs='+',
        help='Integer Array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def sortByBits(self, arr: list) -> list:
        dct = {}
        
        for el in arr:
            n = str(bin(el))[2:]
            n = n.count('1')
            if n not in dct: 
                dct[n] = [el]
            else:
                dct[n].append(el)
                
        result = []

        for el in sorted(dct):
            result += sorted(dct[el])
            
        return result


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1356. Sort Integers by The Number of 1 Bits

You are given an integer array arr. Sort the integers in the array in
ascending order by the number of 1's in their binary representation
and in case of two or more integers have the same number of 1's you
have to sort them in ascending order.

Return the array after sorting it.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1356.py --arr 0 1 2 3 4 5 6 7 8
    >>> [0,1,2,4,8,3,5,6,7]
{Fore.GREEN}
    Explantion:
        [0] is the only integer with 0 bits.
        [1,2,4,8] all have 1 bit.
        [3,5,6] have 2 bits.
        [7] has 3 bits.
    The sorted array by bits is [0,1,2,4,8,3,5,6,7]
{Fore.RESET}
Example 2:
    $ python3 l-1356.py --arr 1024 512 256 128 64 32 16 8 4 2 1
    >>> [1,2,4,8,16,32,64,128,256,512,1024]
{Fore.GREEN}
    Explantion:
        All integers have 1 bit in the binary representation, you
        should just sort them in ascending order.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.arr:
        result = Solution().sortByBits(args.arr)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
