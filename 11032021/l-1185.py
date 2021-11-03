# 1185. Day of the Week


import argparse
from colorama import Fore
from datetime import date


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--day', type=int, nargs=1, help='Day')
	parser.add_argument('--month', type=int, nargs=1, help='Month')
	parser.add_argument('--year', type=int, nargs=1, help='Year')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dct = {6: "Sunday", 
               0:"Monday", 
               1:"Tuesday", 
               2:"Wednesday", 
               3:"Thursday", 
               4:"Friday", 
               5:"Saturday"}
        
        day = date(year, month, day).weekday()
        
        return dct[day]


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 1185. Day of the Week

Given a date, return the corresponding 
day of the week for that date.

The input is given as three integers 
representing the day, month and year respectively.

Return the answer as one of the following values 
["Sunday", "Monday", "Tuesday", "Wednesday", 
"Thursday", "Friday", "Saturday"].
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-1185.py --day 31 --month 8 --year 2019
	>>> "Saturday"

Example 2:
	$ python3 l-1185.py --day 18 --month 7 --year 1999
	>>> "Sunday"

Example 3:
	$ python3 l-1185.py --day 15 --month 8 --year 1993
	>>> "Sunday"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.day and args.month and args.year:
		result = Solution().dayOfTheWeek(args.day[0], args.month[0], args.year[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()