# 1539. Kth Missing Positive Number

from colorama import Fore
import argparse


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-a', '--arr', type=int, nargs='+',
        help='Integer array')

    parser.add_argument('-k', type=int, nargs=1,
        help='Integer K')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def findKthPositive(self, arr: list, k: int) -> int:
        n = 0
        j = 1
        
        if len(arr) == 1:
            el = arr[len(arr)-1]
            
            if k < el:
                return k
            elif k > el:
                return el + (k - el) + 1
            else:
                return el + 1
                

        while n < k:
            if j not in arr:
                n += 1
            if n != k:
                j += 1

        
        return j


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly
increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1539.py --arr 2 3 4 7 11 -k 5
    >>> 9
{Fore.GREEN}
    Explanation:
        The missing positive integers are [1,5,6,8,9,10,12,13,...].
        The 5th missing positive integer is 9.
{Fore.RESET}
Example 2:
    $ python3 l-1539.py --arr 1 2 3 4 -k 2
    >>> 6
{Fore.GREEN}
    Explanation:
        The missing positive integers are [5,6,7,...]. The 2nd missing
        positive integer is
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.arr and args.k:
        result = Solution().findKthPositive(args.arr, args.k[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
