# 26. Remove Duplicates from Sorted Array

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', '--nums', type=int, nargs='+', help='Sorted Array')
    parser.add_argument('-d', '--description', action='store_true', help='Show description')
    parser.add_argument('-e', '--example', action='store_true', help='Show example')

    return parser 


class Solution:
    def removeDuplicates(self, nums):
        new_lst = []
        for el in nums:
            if el not in new_lst:
                new_lst.append(el)

        return f'{len(new_lst)}, nums = {new_lst}'


def main():
    descr = f'''
{Fore.RED}========================================================{Fore.RESET}
{Fore.GREEN}
    # 26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing 
order, remove the duplicates in-place such that each 
unique element appears only once. The relative order 
of the elements should be kept the same.

Since it is impossible to change the length of the 
array in some languages, you must instead have the 
result be placed in the first part of the array nums. 
More formally, if there are k elements after removing 
the duplicates, then the first k elements of nums 
should hold the final result. It does not matter what 
you leave beyond the first k elements.

Return k after placing the final result in the first 
k slots of nums.
{Fore.RESET}
{Fore.RED}========================================================{Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l0026.py --nums 1 1 2
    >>> 2, nums = [1,2,_]
{Fore.GREEN}
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
{Fore.RESET}
Example 2:
    $ python3 l0026.py --nums 0 0 1 1 1 2 2 3 3 4
    >>> 5, nums = [0,1,2,3,4,_,_,_,_,_]
{Fore.GREEN}
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        numbers = args.nums
        result = Solution().removeDuplicates(numbers)
        print(result)

    elif args.description:
        print(descr)

    elif args.example:
        print(example)

    else:
        parser.print_help() 


if __name__=='__main__':
    main()