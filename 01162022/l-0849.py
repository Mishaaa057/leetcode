# 849. Maximize Distance to Closest Person

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', '--seats', type=int, nargs='+',
        help='Integer Array [0, 1]' )
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def maxDistToClosest(self, seats: list) -> int:
        lst = []
        temp = 0
        d = True
        for index, el in enumerate(seats):
            if index == 0 and el == 0:
                d = False
            
            if el == 0:
                temp += 1
            else:
                if temp != 0:
                    if d:
                        if temp % 2 == 0:
                            temp = temp // 2
                        else:
                            temp = temp // 2 + 1

                    lst.append(temp)
                    temp = 0
                    d = True
        if temp:
            lst.append(temp)
        
        return max(lst)


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
# 849. Maximize Distance to Closest Person

You are given an array representing a row of seats where seats[i] = 1
represents a person sitting in the ith seat, and seats[i] = 0
represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and
the closest person to him is maximized. 

Return that maximum distance to the closest person.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0849.py --seats 1 0 0 0 1 0 1
    >>> 2
{Fore.GREEN}
    Explanation: 
    If Alex sits in the second open seat (i.e. seats[2]), then
    the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.
{Fore.RESET}
Example 2
    $ python3 l-0849.py --seats 1 0 0 0
    >>> 3
{Fore.GREEN}
    Explanation: 
    If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.
{Fore.RESET}
Example 3:
    $ python3 l-0849.py --seats 0 1
    >>> 1
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.seats:
        result = Solution().maxDistToClosest(args.seats)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()