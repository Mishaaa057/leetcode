# 1704. Determine if String Halves Are Alike

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
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        counter1 = 0
        counter2 = 0
        
        half1 = s[:len(s)//2]
        half2 = s[len(s)//2:]
        
        for i in range(len(half1)):
            if half1[i] in vowels:
                counter1 += 1
            if half2[i] in vowels:
                counter2 += 1
        
        return counter1 == counter2
            


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1704. Determine if String Halves Are Alike

You are given a string s of even length. Split this string into two
halves of equal lengths, and let a be the first half and b be the
second half.

Two strings are alike if they have the same number of vowels ('a',
'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains
uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1704.py -s "book"
    >>> True
{Fore.GREEN}
    Explanation:
        a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
{Fore.RESET}
Example 2:
    $ python3 l-1704.py -s "textbook"
    >>> False
{Fore.GREEN}
    Explanation:
        a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
        Notice that the vowel o is counted twice. 
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().halvesAreAlike(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
