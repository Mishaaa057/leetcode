# 1848. Minimum Distance to the Target Element


import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', '--nums', type=int, nargs='+',
        help='Integer array')
    parser.add_argument('-s', '--start', type=int, nargs=1,
        help='Integer start')
    parser.add_argument('-t', '--target', type=int, nargs=1,
        help='Integer target')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def getMinDistance(self, nums: list, target: int, start: int) -> int:
        
        results = []
        
        for idx, el in enumerate(nums):
            if el == target:
                results.append(abs(idx - start))
        
        return min(results)


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 1848. Minimum Distance to the Target Element

Given an integer array nums (0-indexed) and two integers target and
start, find an index i such that nums[i] == target and abs(i - start)
is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1848.py --nums 1 2 3 4 5 --target 5 --start 3
    >>> 1
{Fore.GREEN}
    Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
{Fore.RESET}
Example 2:
    $ python3 l-1848.py --nums 1 --target 1 --start 0
    >>> 0
{Fore.GREEN}
    Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.
{Fore.RESET}
Example 3:
    $ python3 l-1848.py --nums 1 1 1 1 1 1 1 1 1 1 1 --target 1 --start 0
    >>> 0
{Fore.GREEN}
    Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums and args.target and args.start:
        result = Solution().getMinDistance(args.nums, args.target[0], args.start[0])
        print(result)

    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
