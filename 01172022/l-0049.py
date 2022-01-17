# 49. Group Anagrams

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', '--strs', type=str, nargs='+',
        help='Strings Array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        dct = {}
        for idx1, el in enumerate(strs):
            if ''.join(sorted(el)) not in dct:
                dct[''.join(sorted(el))] = [el]
            else:
                dct[''.join(sorted(el))].append(el)
        
        return list(dct.values())


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can
return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters
exactly once.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0049.py --strs "eat" "tea" "tan" "ate" "nat" "bat"
    >>> [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    $ python3 l-0049.py --strs "a"
    >>> [["a"]]
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.strs:
        result = Solution().groupAnagrams(args.strs)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
