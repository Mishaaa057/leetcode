# 941. Valid Mountain Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-a', '--arr', type=int, nargs='+',
        help='Integer array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def validMountainArray(self, arr: list) -> bool:
        up = True
        
        for idx, el in enumerate(arr):
            
            if up:
                # if end
                if idx == len(arr)-1:
                    return False
                
                # if next el lower than el
                if idx < len(arr)-1:
                    next = arr[idx+1]
                    if next < el:
                        up = False
                        if idx == 0:
                            return False
                    elif next == el:
                        return False
            
            else:
                # if last
                if idx == len(arr)-1:
                    return True
                
                # if next el bigger than el
                if idx < len(arr)-1:
                    next = arr[idx+1]
                    if next > el:
                        return False
                    elif next == el:
                        return False


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 941. Valid Mountain Array

Given an array of integers arr, return true if and only if it is a
valid mountain array.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0941.py --arr 2 1
    >>> False

Example 2:
    $ python3 l-0941.py --arr 3 5 5
    >>> False

Example 3:
    $ python3 l-0941.py --arr 0 3 2 1
    >>> True
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.arr:
        result = Solution().validMountainArray(args.arr)
        print(result)
    
    elif args.description:
        print(descr)

    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
