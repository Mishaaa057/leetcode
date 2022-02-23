# 1544. Make The String Great

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
    def makeGood(self, s: str) -> str:
        while True:
            l = False
            for idx, el in enumerate(s):

                if idx + 1 <= len(s)-1:
                    el2 = s[idx + 1]
                    check1 = el.isupper() and el2.islower()
                    check2 = el2.isupper() and el.islower()
                    check3 = (el.lower() == el2.lower())

                    if (check1 or check2) and check3:
                        s = s[:idx] + s[idx+2:]
                        l = True
                        break
            if l:
                continue
            
            return s


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1544. Make The String Great

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters
s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in
upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that
make the string bad and remove them. You can keep doing this until
the string becomes good.

Return the string after making it good. The answer is guaranteed to
be unique under the given constraints.

Notice that an empty string is also good.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1544.py -s "leEeetcode"
    >>> "leetcode"
{Fore.GREEN}
    Explanation:
        In the first step, either you choose i = 1 or i = 2, both
        will result "leEeetcode" to be reduced to "leetcode".
{Fore.RESET}
Example 2:
    $ python3 l-1544.py -s "abBAcC"
    >>> ""
{Fore.GREEN}
    Explanation:
        We have many possible scenarios, and all lead to the same
        answer. For example:

        "abBAcC" --> "aAcC" --> "cC" --> ""
        "abBAcC" --> "abBA" --> "aA" --> ""
{Fore.RESET}
Example 3:
    $ python3 l-1544.py -s "s"
Output: "s"
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().makeGood(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
