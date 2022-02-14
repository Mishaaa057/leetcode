# 1957. Delete Characters to Make Fancy String

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-s', type=str, nargs=1,
        help='String S')

    parser.add_argument('-d', '--description', action='store_true',
        help='Sow description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Sow example')
    
    return parser


class Solution:
    def makeFancyString(self, s: str) -> str:
        lst = []
        temp = ''
        for idx, el in enumerate(s):
            if el not in temp:
                if temp != '':
                    lst.append(temp)
                temp = el
            else:
                temp += el
                
            if idx == len(s) - 1:
                lst.append(temp)
        
        result = ''
        for el in lst:
            if len(el) > 2:
                result += (el[0]*2)
            else:
                result += el
        
        return result


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1957. Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are
equal.

Given a string s, delete the minimum possible number of characters
from s to make it fancy.

Return the final string after the deletion. It can be shown that the
answer will always be unique.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1957.py -s "leeetcode"
    >>> "leetcode"
{Fore.GREEN}
    Explanation:
        Remove an 'e' from the first group of 'e's to create "leetcode".
        No three consecutive characters are equal, so return "leetcode".
{Fore.RESET}
Example 2:
    $ python3 l-1957.py -s "aaabaaaa"
    >>> "aabaa"
{Fore.GREEN}
    Explanation:
        Remove an 'a' from the first group of 'a's to create "aabaaaa".
        Remove two 'a's from the second group of 'a's to create "aabaa".
        No three consecutive characters are equal, so return "aabaa".
{Fore.RESET}
Example 3:
    $ python3 l-1957.py -s "aab"
    >>> "aab"
{Fore.GREEN}
    Explanation:
        No three consecutive characters are equal, so return "aab".
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().makeFancyString(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
