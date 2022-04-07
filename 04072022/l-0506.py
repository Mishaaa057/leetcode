# 506. Relative Ranks

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', '--score', type=int, nargs='+',
        help='Integer array score')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser    


class Solution:
    def findRelativeRanks(self, score: list) -> list:
        g = ["Gold Medal",
            "Silver Medal",
            "Bronze Medal"]
        
        res = score.copy()
        
        for i in range(len(score)):
            
            max_idx = score.index(max(score))
            score[max_idx] = -1
            
            if i < len(g):
                res[max_idx] = g[i]
            else:
                res[max_idx] = str(i+1)
        
        return res


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 506. Relative Ranks

You are given an integer array score of size n, where score[i] is the
score of the ith athlete in a competition. All the scores are
guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place
athlete has the highest score, the 2nd place athlete has the 2nd
highest score, and so on. The placement of each athlete determines
their rank:
    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".

For the 4th place to the nth place athlete, their rank is their
placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the
ith athlete.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0506.py --score 5 4 3 2 1
    >>> ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
{Fore.GREEN}
    Explanation:
        The placements are [1st, 2nd, 3rd, 4th, 5th].
{Fore.RESET}
Example 2:
    $ python3 l-0506.py --score 10 3 8 9 4
    >>> ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
{Fore.GREEN}
    Explanation:
        The placements are [1st, 5th, 3rd, 2nd, 4th].
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.score:
        result = Solution().findRelativeRanks(args.score)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
