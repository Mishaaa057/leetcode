# 821. Shortest Distance to a Character

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-s', type=str, nargs=1, help='String s')

    parser.add_argument('-c', type=str, nargs=1, help='Character c')

    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def shortestToChar(self, s: str, c: str) -> list:
        indexes = []
        s = list(s)
        while c in s:
            idx = s.index(c)
            
            indexes.append(idx)
            s[idx] = '_'
        
        for idx, el in enumerate(s):
            if el != '_':
                lower = 9999
                for idx2 in indexes:
                    if lower > abs(idx - idx2):
                        lower = abs(idx - idx2)
                s[idx] = lower
                
            else:
                s[idx] = 0
            
        return s
            


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 821. Shortest Distance to a Character

Given a string s and a character c that occurs in s, return an array
of integers answer where answer.length == s.length and answer[i] is
the distance from index i to the closest occurrence of character c
in s.

The distance between two indices i and j is abs(i - j), where abs is
the absolute value function.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0821.py -s "loveleetcode" -c "e"
    >>> [3,2,1,0,1,0,0,1,2,2,1,0]
{Fore.GREEN}
    Explanation:
    The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
    The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
    The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
    For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
    The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
{Fore.RESET}
Example 2:
    $ python3 l-0821.py -s "aaab" -c "b"
    >>> [3,2,1,0]
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s and args.c:
        result = Solution().shortestToChar(args.s[0], args.c[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
