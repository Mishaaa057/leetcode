# 191. Number of 1 Bits


import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--number', type=int, nargs=1, help='Unsigned Integer')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for el in str(format(n, 'b')):
            if el == '1':
                counter += 1
        
        return counter


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 191. Number of 1 Bits

Write a function that takes an unsigned integer and 
returns the number of '1' bits it has (also known 
as the Hamming weight)
In how many distinct ways can you climb to the top?
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0191.py --number 11
	>>> 3
{Fore.GREEN}
	Explanation: The input number in binary string is 00000000000000000000000000001011 has a total of three '1' bits.
{Fore.RESET}
Example 2:
	$ python3 l-0191.py --number 128
	>>>1
{Fore.GREEN}
	Explanation: The input number in binary string is 00000000000000000000000010000000 has a total of one '1' bit.
{Fore.RESET}
Example 3:
	$ python3 l-0191.py --number 4294967293
	>>> 31
{Fore.GREEN}
	Explanation: The input number in binary string is 11111111111111111111111111111101 has a total of thirty one '1' bits.
{Fore.RESET}
	''' 

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.number:
		result = Solution().hammingWeight(args.number[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()