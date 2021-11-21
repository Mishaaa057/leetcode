# 1450. Number of Students Doing Homework at a Given Time

import argparse 
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-st', '--starttime', type=int, nargs='+', help='Integer array startTime')
	parser.add_argument('-et', '--endtime', type=int, nargs='+', help='Integer array endTime')
	parser.add_argument('-qt', '--querytime', type=int, nargs=1, help='Query time')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def busyStudent(self, startTime: list, endTime: list, queryTime: int) -> int:
        counter = 0
        for index, el in enumerate(startTime):
            if el <= queryTime <= endTime[index]:
                counter += 1
        
        return counter 


def main():
	descr = f'''
{Fore.RED}=================================================================={Fore.RESET}
{Fore.GREEN}
	# 1450. Number of Students Doing 
	      Homework at a Given Time

Given two integer arrays startTime and endTime and given 
an integer queryTime.

The ith student started doing their homework at the time 
startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time 
queryTime. More formally, return the number of students 
where queryTime lays in the interval [startTime[i], endTime[i]] 
inclusive.
{Fore.RESET}
{Fore.RED}=================================================================={Fore.RESET}
	'''
	
	example = f'''
Example 1:
	$ python3 l-1450.py  --starttime 1 2 3 --endtime 3 2 7 --querytime 4
	>>> 1
{Fore.GREEN}
	Explanation: We have 3 students where:
	The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
	The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
	The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
{Fore.RESET}
Example 2:
	$ python3 l-1450.py --starttime 4 --endtime 4 --querytime 4
	>>> 1
{Fore.GREEN}
	Explanation: The only student was doing their homework at the queryTime.
{Fore.RESET}
Example 3:
	$ python3 l-1450.py --starttime 4 --endtime 4 --querytime 5
	>>> 0

Example 4:
	$ python3 l-1450.py --starttime 1 1 1 1 --endtime 1 3 2 4 --querytime 7
	>>> 0

Example 5:
	$ python3 l-1450.py --starttime 9 8 7 6 5 4 3 2 1 --endtime 10 10 10 10 10 10 10 10 10 --querytime 5
	>>> 5
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.starttime and args.endtime and args.querytime and len(args.starttime) == len(args.endtime):
		result = Solution().busyStudent(args.starttime, args.endtime, args.querytime[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
