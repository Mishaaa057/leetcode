# 2042. Check if Numbers Are Ascending in a Sentence

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-s', type=str, nargs=1, help='String s')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lst = s.split(' ')
        
        nums = []
        
        for el in lst:
            if el.isdigit():
                if int(el) not in nums:
                    nums.append(int(el))
                else:
                    return False
        
        return nums == sorted(nums)


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2042. Check if Numbers Are Ascending in a Sentence

A sentence is a list of tokens separated by a single space with no
leading or trailing spaces. Every token is either a positive number
consisting of digits 0-9 with no leading zeros, or a word consisting
of lowercase English letters.

For example, "a puppy has 2 eyes 4 legs" is a sentence with seven
tokens: "2" and "4" are numbers and the other tokens such as "puppy"
are words.
Given a string s representing a sentence, you need to check if all
the numbers in s are strictly increasing from left to right (i.e.,
other than the last number, each number is strictly smaller than the
number on its right in s).

Return true if so, or false otherwise.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2042.py -s "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
    >>> True
{Fore.GREEN}
    Explanation:
        The numbers in s are: 1, 3, 4, 6, 12.
        They are strictly increasing from left to right:
            1 < 3 < 4 < 6 < 12.
{Fore.RESET}
Example 2:
    $ python3 l-2042.py -s "hello world 5 x 5"
    >>> False
{Fore.GREEN}
    Explanation:
        The numbers in s are: 5, 5. They are not strictly increasing.
{Fore.RESET}
Example 3:
    $ python3 l-2042.py -s "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
    >>> False
{Fore.GREEN}
    Explanation:
        The numbers in s are: 7, 51, 50, 60.
        They are not strictly increasing.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().areNumbersAscending(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
