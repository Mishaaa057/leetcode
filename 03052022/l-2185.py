# 2185. Counting Words With a Given Prefix

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-w', '--words', type=str, nargs='+',
        help='Words array')
    parser.add_argument('-p', '--pref', type=str, nargs=1,
        help='Prefix')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def prefixCount(self, words: list, pref: str) -> int:
        counter = 0 
        for idx, word in enumerate(words):
            n = len(pref)
            
            if word[:n] == pref:
                counter += 1
        
        return counter


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 2185. Counting Words With a Given Prefix

You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2185.py --words "pay" "attention" "practice" "attend" --pref "at"
    >>> 2
{Fore.GREEN}
    Explanation:
        The 2 strings that contain "at" as a prefix are: "attention" and "attend".
{Fore.RESET}
Example 2:
    $ python3 l-2185.py --words "leetcode" "win" "loops" "success" --pref "code"
    >>> 0
{Fore.GREEN}
    Explanation:
        There are no strings that contain "code" as a prefix.
{Fore.RESET}
    '''
    
    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.words and args.pref:
        result = Solution().prefixCount(args.words, args.pref[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
