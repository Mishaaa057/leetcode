# 1137. N-th Tribonacci Number


from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', nargs=1, type=int, help='Number')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def tribonacci(self, n: int) -> int:
        lst = [0, 1, 1]
        for i in range(n+1):
            if i + 1 > len(lst):
                new = lst[i-3] + lst[i-2] + lst[i-1]
                lst.append(new)
            
        return lst[n]


def main():
	descr = f'''
{Fore.RED}================================================================={Fore.RESET}
	{Fore.GREEN}# 1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.{Fore.RESET}
{Fore.RED}================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1137.py -n 4
	>>> 4
	{Fore.GREEN}
	Explanation:
	T_3 = 0 + 1 + 1 = 2
	T_4 = 1 + 1 + 2 = 4
	{Fore.RESET}
Example 2:
	$ python3 l-1137.py -n 25
	>>> 1389537
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.n:
		result = Solution().tribonacci(args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()