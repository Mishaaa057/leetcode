# 2176. Count Equal and Divisible Pairs in an Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', '--nums', nargs='+', type=int,
        help='Integer array')
    parser.add_argument('-k', type=int, nargs=1,
        help='Integer K')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def countPairs(self, nums: list, k: int) -> int:
        
        counter = 0 
        
        for idx1, el1 in enumerate(nums):
            for idx2, el2 in enumerate(nums[idx1 + 1:]):
                idx2 = idx2 + idx1 + 1
                
                if (idx1 * idx2) % k == 0 and el1 == el2:
                    counter += 1
    
        return counter


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 2176. Count Equal and Divisible Pairs in an Array

Given a 0-indexed integer array nums of length n and an integer k,
return the number of pairs (i, j) where 0 <= i < j < n, such that
nums[i] == nums[j] and (i * j) is divisible by k.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2176.py --nums 3 1 2 2 2 1 3 -k 2
    >>> 4
{Fore.GREEN}
    Explanation:
    There are 4 pairs that meet all the requirements:
        - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
        - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
        - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
        - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
{Fore.RESET}
Example 2:
    $ python3 l-2176.py --nums 1 2 3 4 -k 1
    >>> 0
{Fore.GREEN}
    Explanation:
        Since no value in nums is repeated, there are no pairs (i,j) that
        meet all the requirements.
{Fore.RESET}
    '''
    
    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums and args.k:
        result = Solution().countPairs(args.nums, args.k[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
