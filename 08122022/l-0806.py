# 806. Number of Lines To Write String

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-w', '--widths', type=int, nargs='+', metavar='--widths [widths]', 
        help='array widths denoting how many pixels wide each lowercase English letter is')
    parser.add_argument('-s', type=str, nargs=1, metavar='-s STRING',
        help='string s of lowercase English letters')
    parser.add_argument('-d', '--description', action='store_true',
        help='show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='show example')
    
    return parser


class Solution:
    def numberOfLines(self, widths:list, s: str) -> list:
        lines = 1
        n = 0
        
        for letter in s:
            width = widths[ord(letter) - 97]
            
            if n + width <= 100:
                n += width
                
                
            else:
                lines += 1
                n = width
            
            
        return [lines, n]


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
    # 806. Number of Lines To Write String

You are given a string s of lowercase English letters and an array
widths denoting how many pixels wide each lowercase English letter
is. Specifically, widths[0] is the width of 'a', widths[1] is the
width of 'b', and so on.

You are trying to write s across several lines, where each line is
no longer than 100 pixels. Starting at the beginning of s, write as
many letters on the first line such that the total width does not
exceed 100 pixels. Then, from where you stopped in s, continue
writing as many letters as you can on the second line. Continue this
process until you have written all of s.

Return an array result of length 2 where:

result[0] is the total number of lines.
result[1] is the width of the last line in pixels.
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:

    $ python3 l-0806.py --widths 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 -s "abcdefghijklmnopqrstuvwxyz"
    >>> [3,60]
{Fore.GREEN}
    Explanation: You can write s as follows:
        abcdefghij  // 100 pixels wide
        klmnopqrst  // 100 pixels wide
        uvwxyz      // 60 pixels wide
        There are a total of 3 lines, and the last line is 60 pixels wide.
{Fore.RESET}
Example 2:
        $ python3 l-0806.py --widths 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 -s "bbbcccdddaaa"
    >>> [2,4]
{Fore.GREEN}
    Explanation: You can write s as follows:
        bbbcccdddaa  // 98 pixels wide
        a            // 4 pixels wide
        There are a total of 2 lines, and the last line is 4 pixels wide.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s and args.widths:
        result = Solution().numberOfLines(widths = args.widths,s=args.s[0])
        print(result)

    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
