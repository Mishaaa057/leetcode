# 70. Climbing Stairs


import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--number', type=int, nargs=1, help='Number of steps')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def climbStairs(self, n: int) -> int:
        # Its a progression An = An-1 + An-2
        # An-1 it is last element of list, An-2 it is penultimate element of list
        lst = [1, 2, 3]
        
        while n > len(lst): 
            penultimate_element = lst[len(lst) - 2]
            last_element = lst[len(lst) - 1]
            
            lst.append(penultimate_element + last_element)
        
        return lst[n - 1]
    

def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 70. Climbing Stairs

You are climbing a staircase. It takes n steps 
to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0070.py --number 2
	>>> 2
{Fore.GREEN}
	Explanation: There are two ways to climb to the top.
	1. 1 step + 1 step
	2. 2 steps
{Fore.RESET}
Example 2:
	$ python3 l-0070.py --number 3
	>>>3
{Fore.GREEN}
	Explanation: There are three ways to climb to the top.
	1. 1 step + 1 step + 1 step
	2. 1 step + 2 steps
	3. 2 steps + 1 step
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.number:
		result = Solution().climbStairs(args.number[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()