# 693. Binary Number with Alternating Bits


from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--number', '-n', nargs=1,
		type=int, metavar='n',
		help='Some integer')
	parser.add_argument('--description', '-d',
		action='store_true', help='Show description')
	parser.add_argument('--example', '-e',
		action='store_true', help='Show example')

	return parser



class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)
        
        for index, el in enumerate(bin_n):
            if index < len(bin_n) - 1:
                if el == bin_n[index + 1]:
                    return False
        
        return True


def Main():
	g = Fore.GREEN
	r = Fore.RED
	reset = Fore.RESET

	descr = f'''
{r}=================================================={reset}
{g} 693. Binary Number with Alternating Bits

Given a positive integer, check whether it has
alternating bits: namely, if two adjacent bits 
will always have different values.{reset}
{r}=================================================={reset}
	'''

	example = f'''
Example 1:
	$ python3 --number 5
	>>> true
	
	{g}Explanation: The binary representation of 5 is: 101{reset}

Example 2:
	python3 --number 7
	>>> false
	
	{g}Explanation: The binary representation of 7 is: 111.{reset}

Example 3:
	python3 --number 11
	>>> false
	
	{g}Explanation: The binary representation of 11 is: 1011.{reset}

Example 4:
	python3 --number 10
	>>> true
	
	{g}Explanation: The binary representation of 10 is: 1010.{reset}

Example 5:

	python3 --number 3
	>>> false
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()


	if args.number:
		result = Solution().hasAlternatingBits(args.number[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__ == '__main__':
	Main()