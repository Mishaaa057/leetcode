# 2259. Remove Digit From Number to Maximize Result

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-n', '--number', type=str, nargs=1,
        help='Number')
    parser.add_argument('--digit', type=str, nargs=1,
        help='Digit')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        lst = []
        
        for idx, el in enumerate(number):
            if el == digit:
                lst.append(int(number[:idx] + number[idx+1:]))
        
        return str(max(lst))


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2259. Remove Digit From Number to Maximize Result

You are given a string number representing a positive integer and a
character digit.

Return the resulting string after removing exactly one occurrence of
digit from number such that the value of the resulting string in
decimal form is maximized. The test cases are generated such that
digit occurs at least once in number.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2259.py --number "123" --digit "3"
    >>> "12"
{Fore.GREEN}
    Explanation:
        There is only one '3' in "123". After removing '3', the result is "12".
{Fore.RESET}
Example 2:
    $ python3 l-2259.py --number "1231" --digit "1"
    >>> "231"
{Fore.GREEN}
    Explanation:
        We can remove the first '1' to get "231" or remove the second '1' to get "123".
        
        Since 231 > 123, we return "231".
{Fore.RESET}
Example 3:
    $ python3 l-2259.py --number "551" --digit "5"
    >>> "51"
{Fore.GREEN}
    Explanation:
        We can remove either the first or second '5' from "551".
        Both result in the string "51".
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.number and args.digit:
        result = Solution().removeDigit(args.number[0], args.digit[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
