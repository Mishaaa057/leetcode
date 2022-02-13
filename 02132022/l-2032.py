# 2032. Two Out of Three

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n1', '--nums1', type=int, nargs='+',
        help='Integer array 1')
    parser.add_argument('-n2', '--nums2', type=int, nargs='+',
        help='Integer array 2')
    parser.add_argument('-n3', '--nums3', type=int, nargs='+',
        help='Integer array 3')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def twoOutOfThree(self, nums1: list, nums2: list, nums3: list) -> list:
        nums_set = [nums1, nums2, nums3]
        
        dct = {}
        
        for nums in nums_set:
            nums = list(dict.fromkeys(nums))
            for el in nums:
                if el not in dct:
                    dct[el] = 1
                else:
                    dct[el] += 1
            
        result = []
        
        for key in dct:
            if dct[key] >= 2:
                result.append(key)
        
        return result
                    

def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2032. Two Out of Three

Given three integer arrays nums1, nums2, and nums3, return a distinct
array containing all the values that are present in at least two out
of the three arrays. You may return the values in any order.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2032.py --nums1 1 1 3 2 --nums2 2 3 --nums3 3
    >>> [3,2]
{Fore.GREEN}
    Explanation: 
        The values that are present in at least two arrays are:
            - 3, in all three arrays.
            - 2, in nums1 and nums2.
{Fore.RESET}
Example 2:
    $ python3 l-2032.py --nums1 3 1 --nums2 2 3 --nums3 1 2
    >>> [2,3,1]
{Fore.GREEN}
    Explanation:
        The values that are present in at least two arrays are:
        - 2, in nums2 and nums3.
        - 3, in nums1 and nums2.
        - 1, in nums1 and nums3.
{Fore.RESET}
Example 3:
    $ python3 l-2032.py --nums1 1 2 2 --nums2 4 3 3 --nums3 5
    >>> []
{Fore.GREEN}
    Explanation:
        No value is present in at least two arrays.
 {Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums1 and args.nums2 and args.nums3:
        result = Solution().twoOutOfThree(args.nums1, args.nums2, args.nums3)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
