# 682. Baseball Game

import argparse
from colorama import Fore
from pandas import describe_option


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-o', '--ops', type=str, nargs='+',
        help='String array')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def calPoints(self, ops: list) -> int:
        res = []
        
        for el in ops:
            if el == '+':
                res.append(sum(res[-2:]))
                
            elif el == 'D':
                res.append(res[len(res)-1] * 2)
            
            elif el == 'C':
                res.pop(len(res)-1)
            
            else:
                res.append(int(el))
        
        return sum(res)


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 682. Baseball Game

You are keeping score for a baseball game with strange rules. The
game consists of several rounds, where the scores of past rounds may
affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are
given a list of strings ops, where ops[i] is the ith operation you
must apply to the record and is one of the following:

    An integer x - Record a new score of x.

    "+" - Record a new score that is the sum of the previous two
    scores. It is guaranteed there will always be two previous scores.

    "D" - Record a new score that is double the previous score. It is
    guaranteed there will always be a previous score.

    "C" - Invalidate the previous score, removing it from the record.
    It is guaranteed there will always be a previous score.

Return the sum of all the scores on the record.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''
    
    example = f'''
Example 1:
    $ python3 l-0682.py --ops "5" "2" "C" "D" "+"
    >>> 30
{Fore.GREEN}
    Explanation:
        "5" - Add 5 to the record, record is now [5].
        "2" - Add 2 to the record, record is now [5, 2].
        "C" - Invalidate and remove the previous score, record is now [5].
        "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
        "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
    The total sum is 5 + 10 + 15 = 30.
{Fore.RESET}
Example 2:
    $ python3 l-0682.py --ops "5" "-2" "4" "C" "D" "9" "+" "+"
    >>> 27
{Fore.GREEN}
    Explanation:
        "5" - Add 5 to the record, record is now [5].
        "-2" - Add -2 to the record, record is now [5, -2].
        "4" - Add 4 to the record, record is now [5, -2, 4].
        "C" - Invalidate and remove the previous score, record is now [5, -2].
        "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
        "9" - Add 9 to the record, record is now [5, -2, -4, 9].
        "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
        "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
    The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
{Fore.RESET}
Example 3:
    $ python3 l-0682.py --ops "1"
    >>> 1
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.ops:
        result = Solution().calPoints(args.ops)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
