# 3. Longest Substring Without Repeating Characters

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
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        
        results = []
        for idx1, el1 in enumerate(s):
            temp = el1
            for idx2, el2 in enumerate(s[idx1+1:]):
                idx2 = idx2 + idx1+1
                    
                if el2 not in temp:
                    temp += el2
                else:
                    break
                    
            results.append(len(temp))
        
        return max(results)
            
            

def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without
repeating characters.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0003.py -s "abcabcbb"
    >>> 3
{Fore.GREEN}
    Explanation:
        The answer is "abc", with the length of 3.
{Fore.RESET}
Example 2:
    $ python3 l-0003.py -s "bbbbb"
    >>> 1
{Fore.GREEN}
    Explanation:
        The answer is "b", with the length of 1.
{Fore.RESET}
Example 3:
    $ python3 l-0003.py -s "pwwkew"
    >>> 3
{Fore.GREEN}
    Explanation:
        The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a
        subsequence and not a substring.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().lengthOfLongestSubstring(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
