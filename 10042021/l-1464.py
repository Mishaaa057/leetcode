# 1464. Maximum Product of Two Elements in an Arra


import argparse
from colorama import Fore as F


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-a', '--array', metavar='n', nargs='+', type=int, help='Integer array')
    parser.add_argument('-d', '--description', action='store_true', help='Show description')
    parser.add_argument('-e', '--example', action='store_true', help='Show example')

    return parser 



class Solution:
    def maxProduct(self, nums: list) -> int:
        max_num = max(nums)
        nums.remove(max_num)
        next_max = max(nums) 
        return (max_num-1) * (next_max-1)



def main():
    descr = f'''
{F.RED}============================================================================={F.RESET}
{F.GREEN}
    # 1464. Maximum Product of Two Elements in an Arra

Given the array of integers nums, you will choose two different indices 
i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
{F.RESET}
{F.RED}============================================================================={F.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1464.py --array 3 4 5 2
    >>> 12 
{F.GREEN}
    Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
    you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
{F.RESET}
Example 2:
    $ python3 l-1464.py --array 1 5 4 5
    >>> 16
{F.GREEN}
    Explanation: Choosing the indices i=1 and j=3 (indexed from 0), 
    you will get the maximum value of (5-1)*(5-1) = 16.
{F.RESET}
Example 3:
    $ python3 l-1464.py --array 3 7
    >>> 12
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.array:
        result = Solution().maxProduct(args.array)
        print(result)

    elif args.description:
        print(descr)

    elif args.example:
        print(example)

    else:
        parser.print_help()


if __name__=='__main__':
    main()