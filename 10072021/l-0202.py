# 202. Happy Number


import argparse
from colorama import Fore


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', type=int, nargs='+', help='Some Number')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def isHappy(self, n: int) -> bool:
        if n > 0:
            if n == 1:
                return True
            lst = []
            while n != 1:
                if n not in lst:
                    lst.append(n)

                    numbers_lst = []
                    for number in str(n):
                        numbers_lst.append(int(number))

                    result_num = 0
                    for el in numbers_lst:
                        result_num += el ** 2
                    
                    n = result_num
                    
                    if n == 1:
                        return True
                else:
                    break
        return False
        

def main():
	descr = f'''
{Fore.RED}========================================================================{Fore.RESET}
{Fore.GREEN}
	# 202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the 
sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
{Fore.RESET}
{Fore.RED}========================================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0202.py -n 19
	>>> True
{Fore.GREEN}
	Explanation:
		12 + 92 = 82
		82 + 22 = 68
		62 + 82 = 100
		12 + 02 + 02 = 1
{Fore.RESET}
Example 2:
	$ python3 l-0202.py -n 2
	>>> False
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.n:
		for n in args.n:
			result = Solution().isHappy(n)
			print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
