# 1588. Sum of All Odd Length Subarrays

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
    def sumOddLengthSubarrays(self, arr: list) -> int:
        
        result = 0
        
        for n in range(1, len(arr) + 1):
            if n % 2 != 0:
                for idx, el in enumerate(arr):
                    if idx + n <= len(arr):
                        temp = arr[idx:]
                        temp = temp[:n]
                        result += sum(temp)
        
        return result


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1588. Sum of All Odd Length Subarrays

Given an array of positive integers arr, calculate the sum of all
possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1588.py --arr 1 4 2 5 3
    >>> 58
{Fore.GREEN}
    Explanation:
        The odd-length subarrays of arr and their sums are:
            [1] = 1
            [4] = 4
            [2] = 2
            [5] = 5
            [3] = 3
            [1,4,2] = 7
            [4,2,5] = 11
            [2,5,3] = 10
            [1,4,2,5,3] = 15
            If we add all these together we get 1 + 4 + 2 + 5 + 3 +
                7 + 11 + 10 + 15 = 58
{Fore.RESET}
Example 2:
    $ python3 l-1588.py --arr 1 2
    >>> 3
{Fore.GREEN}
    Explanation:
        There are only 2 subarrays of odd length, [1] and [2]. Their
        sum is 3.
{Fore.RESET}
Example 3:
    $ python3 l-1588.py --arr 10 11 12
    >>> 66
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.arr:
        result = Solution().sumOddLengthSubarrays(args.arr)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
