# 461. Hamming Distance

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-x', type=int, nargs=1, metavar='N', help='An integer X')
	parser.add_argument('-y', type=int, nargs=1, metavar='N', help='An integer Y')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = ("{0:b}".format(x))
        y = ("{0:b}".format(y))
        
        if len(x) != len(y):
            n = abs(len(y) - len(x))
            
            if len(x) < len(y):
                x = ('0' * n) + x
            
            elif len(y) < len(x):
                y = ('0' * n) + y
            
        counter = 0
        for index, el in enumerate(x):
            if y[index] != el:
                counter += 1
        
        return counter 


def main():
	descr = f'''
{Fore.RED}============================================================{Fore.RESET}
{Fore.GREEN}
	# 461. Hamming Distance

The Hamming distance between two integers is the number of 
positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance
between them.
{Fore.RESET}
{Fore.RED}============================================================{Fore.RESET}
	'''
	
	example = f'''
Example 1:
	$ python3 l-0461.py -x 1 -y 4
	>>> 2
{Fore.GREEN}
	Explanation:
	1   (0 0 0 1)
	4   (0 1 0 0)
	       ↑   ↑
	The above arrows point to positions where the corresponding bits are different.
{Fore.RESET}
Example 2:
	$ python3 l-0461.py -x 3 -y 1
	>>> 1
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.x and args.y:
		result = Solution().hammingDistance(args.x[0], args.y[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
