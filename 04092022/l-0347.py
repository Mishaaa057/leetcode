# 347. Top K Frequent Elements

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-n', '--nums', type=int, nargs="+",
        help='Integer array nums')
    parser.add_argument('-k', type=int, nargs=1,
        help='Integer K')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        lst = []
        length = []
        
        for el in nums:
            if el not in lst:
                length.append(nums.count(el))
                lst.append(el)
        
        result = []
        while k > 0:
            
            idx = length.index(max(length))
            result.append(lst[idx])
            length.pop(idx)
            lst.pop(idx)
            
            k -= 1
        
        return result


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most
frequent elements. You may return the answer in any order.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0347.py --nums 1 1 1 2 2 3 -k 2
    >>> [1,2]

Example 2:
    $ python3 l-0347.py --nums 1 -k 1
    >>> [1]
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums and args.k:
        result = Solution().topKFrequent(args.nums, args.k[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
