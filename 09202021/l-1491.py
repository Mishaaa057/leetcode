# 1491. Average Salary Excluding the Minimum and Maximum Salary


from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--salary', '-s',
		nargs='+', type=int, help='Integer array')
	parser.add_argument('--description', '-d', action='store_true',
		help='Show description')
	parser.add_argument('--example', '-e', action='store_true',
		help='Show example')

	return parser 


class Solution:
    def average(self, salary):
        salary.remove(max(salary))
        salary.remove(min(salary))
        
        return sum(salary) / len(salary)


def Main():
	descr = f'''
{Fore.RED}====================================================={Fore.RESET}
	{Fore.GREEN}# 1491. Average Salary Excluding the 
	  Minimum and Maximum Salary

Given an array of unique integers salary where 
salary[i] is the salary of the employee i.

Return the average salary of employees excluding 
the minimum and maximum salary.{Fore.RESET}
{Fore.RED}====================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1491.py --salary 4000 3000 1000 2000
	>>> 2500.00000

	{Fore.GREEN}Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
	Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500{Fore.RESET}

Example 2:
	$ python3 l-1491.py --salary 1000 2000 3000
	>>> 2000.00000

	{Fore.GREEN}Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
	Average salary excluding minimum and maximum salary is (2000)/1= 2000{Fore.RESET}

Example 3:
	$ python3 l-1491.py --salary 6000 5000 4000 3000 2000 1000
	>>> 3500.00000

Example 4:
	$ python3 l-1491.py --salary 8000 9000 2000 3000 6000 1000
	>>> 4750.00000
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.salary:
		result = Solution().average(args.salary)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()