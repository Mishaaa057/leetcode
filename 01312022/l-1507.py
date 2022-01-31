# 1507. Reformat Date

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('--date', type=str, nargs=1,
        help='Date')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def reformatDate(self, date: str) -> str:
        lst = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        date = date.split(' ')
        
        day = date[0][:-2]
        if len(day) < 2:
            day = '0' + day
        
        month = lst.index(date[1]) + 1
        if month < 10:
            month = '0' + str(month)
        
        year = date[2]
        
        result = f'{year}-{month}-{day}'
        return result
        


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1507. Reformat Date

Given a date string in the form Day Month Year, where:
    Day is in the set ["1st", "2nd", "3rd", "4th", ...,
        "30th", "31st"].
    Month is in the set ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul","Aug", "Sep", "Oct", "Nov", "Dec"].
    Year is in the range [1900, 2100].
    
Convert the date string to the format YYYY-MM-DD, where:
    YYYY denotes the 4 digit year.
    MM denotes the 2 digit month.
    DD denotes the 2 digit day.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-1507.py --date "20th Oct 2052"
    >>> "2052-10-20"

Example 2:
    $ python3 l-1507.py --date "6th Jun 1933"
    >>> "1933-06-06"

Example 3:
    $ python3 l-1507.py --date "26th May 1960"
    >>> "1960-05-26"
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.date:
        result = Solution().reformatDate(args.date[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
