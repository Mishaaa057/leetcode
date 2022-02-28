# 551. Student Attendance Record I

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
    def checkRecord(self, s: str) -> bool:
        dct = {
            'A': [],
            'L': [],
            'P': [],
        }
        
        temp = s[0]
        counter = 1
        
        for idx, el in enumerate(s[1:]):
            if el == temp:
                counter += 1
            else:
                dct[temp].append(counter)
                temp = el
                counter = 1
            
            if idx == len(s[1:])-1:
                dct[temp].append(counter)
        
        if dct['A']:
            if sum(dct["A"]) >= 2:
                return False
        
        if dct['L']:
            for el in dct['L']:
                if el >= 3:
                    return False
        
        return True
            

def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 551. Student Attendance Record I

You are given a string s representing an attendance record for a
student where each character signifies whether the student was
absent, late, or present on that day. The record only contains
the following three characters:

    'A': Absent.
    'L': Late.
    'P': Present.

The student is eligible for an attendance award if they meet both
of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or
false otherwise.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0551.py -s "PPALLP"
    >>> True
{Fore.GREEN}
    Explanation:
        The student has fewer than 2 absences and was never late
        3 or more consecutive days.
{Fore.RESET}
Example 2:
    $ python3 l-0551.py -s "PPALLL"
    >>> False
{Fore.GREEN}
    Explanation:
        The student was late 3 consecutive days in the last 3 days,
        so is not eligible for the award.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.s:
        result = Solution().checkRecord(args.s[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
