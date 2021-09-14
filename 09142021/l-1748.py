# 1748. Sum of Unique Elements


from colorama import Fore
import argparse


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument("--nums", "-n", metavar="n",
            type=int,
            nargs="+", help="Integer array")
    parser.add_argument("--description", "-d",
            action="store_true",
            help="Show description")
    parser.add_argument("--example", "-e",
            action="store_true",
            help="Show some examples")

    return parser


class Solution():
    def sumOfUnique(self, nums):
        lst = []
        dct = {}

        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1

        for key in dct:
            if dct[key] == 1:
                lst.append(key)

        return sum(lst)


def Main():
    descr = f"""{Fore.GREEN}
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
{Fore.RESET}
    """

    example = """
Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
    """

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.nums:
        result = Solution().sumOfUnique(args.nums)
        print(result)

    elif args.description:
        print(descr)

    elif args.example:
        print(example)

    else:
        parser.print_help()


if __name__=="__main__":
    Main()
