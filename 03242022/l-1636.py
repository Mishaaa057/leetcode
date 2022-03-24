# 1636. Sort Array by Increasing Frequency

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-n','--nums', nargs='+', type=int,
        help="Integer array")
    
    parser.add_argument('-d', '--description', action='store_true',
        help="Show description")
    parser.add_argument('-e', '--example', action='store_true',
        help="Show example")
    
    return parser


class Solution:
    def frequencySort(self, nums: list) -> list:
        dct = {}
        
        for el in nums:
            n = nums.count(el)
            
            if n not in dct:
                dct[n] = [el]
            else:
                dct[n].append(el)
                dct[n] = sorted(dct[n])[::-1]
        
        res = []
        for key in sorted(dct.keys()):
            res += dct[key]
        
        return res


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 1636. Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order
based on the frequency of the values. If multiple values have the
same frequency, sort them in decreasing order.

Return the sorted array.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1636.py --nums 1 1 2 2 2 3
    >>> [3,1,1,2,2,2]
{Fore.GREEN}
    Explanation:
        '3' has a frequency of 1, '1' has a frequency of 2, and
        '2' has a frequency of 3.
{Fore.RESET}
Example 2:
    $ python3 l-1636.py --nums 2 3 1 3 2
    >>> [1,3,3,2,2]
{Fore.GREEN}
    Explanation:
        '2' and '3' both have a frequency of 2, so
        they are sorted in decreasing order.
{Fore.RESET}
Example 3:
    $ python3 l-1636.py --nums -1 1 -6 4 5 -6 1 4 1
    >>> [5,-1,4,4,-6,-6,1,1,1]
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().frequencySort(args.nums)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
