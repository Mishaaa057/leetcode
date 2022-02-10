# 2085. Count Common Words With One Occurrence

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-w1', '--words1', type=str, nargs='+',
        help='Words 1 Array')
    parser.add_argument('-w2', '--words2', type=str, nargs='+',
        help='Words 2 Array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')    
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')    
    
    return parser


class Solution:
    def countWords(self, words1: list, words2: list) -> int:
        dct1 = {}
        dct2 = {}
        
        for el in words1:
            if el not in dct1:
                dct1[el] = 1
            else:
                dct1[el] += 1
                
        for el in words2:
            if el not in dct2:
                dct2[el] = 1
            else:
                dct2[el] += 1
        
        lst = []
        result = []
        
        for el in dct1:
            if dct1[el] == 1:
                lst.append(el)

        for el in dct2:
            if dct2[el] == 1:
                if el in lst:
                    result.append(el)
        
        return len(result)


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2085. Count Common Words With One Occurrence

Given two string arrays words1 and words2, return the number of
strings that appear exactly once in each of the two arrays.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2085.py --words1 "leetcode" "is" "amazing" "as" "is" --words2 "amazing" "leetcode" "is"
    >>> 2
{Fore.GREEN}
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
{Fore.RESET}
Example 2:
    $ python3 l-2085.py --words1 "b" "bb" "bbb" --words2 "a" "aa" "aaa"
    >>> 0
{Fore.GREEN}
Explanation: 
There are no strings that appear in each of the two arrays.
{Fore.RESET}
Example 3:
    $ python3 l-2085.py --words1 "a" "ab" --words2 ["a" "a" "a" "ab"
    >>> 1
{Fore.GREEN}
Explanation:
The only string that appears exactly once in each of the two arrays is "ab".
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.words1 and args.words2:
        result = Solution().countWords(args.words1, args.words2)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
