# 2138. Divide a String Into Groups of Size k

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', type=str, nargs=1,
        help='String')
    parser.add_argument('-k', type=int, nargs=1,
        help='Integer K')
    parser.add_argument('-f', '--fill', type=str, nargs=1,
        help='Fill character')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list:
        result = []
        
        while True:
            if len(s) >= k:
                group = s[:k]
                s = s[k:]
                result.append(group)
            else:
                group = s
                if group != '':
                    group += fill * (k - len(group))
                    result.append(group)
                break
        
        return result


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 2138. Divide a String Into Groups of Size k

A string s can be partitioned into groups of size k using the
following procedure:

The first group consists of the first k characters of the string, the
second group consists of the next k characters of the string, and so
on. Each character can be a part of exactly one group.
For the last group, if the string does not have k characters
remaining, a character fill is used to complete the group.
Note that the partition is done so that after removing the fill
character from the last group (if it exists) and concatenating all
the groups in order, the resultant string should be s.

Given the string s, the size of each group k and the character fill,
return a string array denoting the composition of every group s has
been divided into, using the above procedure.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2138.py -s "abcdefghi" -k 3 --fill "x"
    >>> ["abc","def","ghi"]
{Fore.GREEN}
    Explanation:
    The first 3 characters "abc" form the first group.
    The next 3 characters "def" form the second group.
    The last 3 characters "ghi" form the third group.
    Since all groups can be completely filled by characters from the
        string, we do not need to use fill.
    Thus, the groups formed are "abc", "def", and "ghi".
{Fore.RESET}
Example 2:
    $ python3 l-2138.py -s "abcdefghij" -k 3 --fill "x"
    >>> ["abc","def","ghi","jxx"]
{Fore.GREEN}
    Explanation:
    Similar to the previous example, we are forming the first three
        groups "abc", "def", and "ghi".
    For the last group, we can only use the character 'j' from the
        string. To complete this group, we add 'x' twice.
    Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s and args.k and args.fill:
        result = Solution().divideString(args.s[0], args.k[0], args.fill[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
