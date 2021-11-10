# 1281. Subtract the Product and Sum of Digits of an Integer

from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--number', nargs=1, type=int, help='Integer number n')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits_list = list(str(n))
        product = None
        digits_sum = 0

        for el in digits_list:
        	# Get product of digits
            if '0' not in digits_list:
                if product:
                    product = product * int(el)
                else:
                    product = int(el)
            else:
                product = 0
            
            
            # Get sum of digits
            digits_sum += int(el)

        # Generate result
        result = product - digits_sum
        return result


def main():
	descr = f'''
{Fore.RED}====================================================={Fore.RESET}
{Fore.GREEN}
	# 1281. Subtract the Product and 
	   Sum of Digits of an Integer

Given an integer number n, return the difference 
between the product of its digits and 
the sum of its digits.
{Fore.RESET}
{Fore.RED}====================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1281.py --number 234
	>>> 15 
{Fore.GREEN}
	Explanation: 
	Product of digits = 2 * 3 * 4 = 24 
	Sum of digits = 2 + 3 + 4 = 9 
	Result = 24 - 9 = 15
{Fore.RESET}
Example 2:
	$ python3 l-1281.py --number 4421
	>>> 21
{Fore.GREEN}
	Explanation: 
	Product of digits = 4 * 4 * 2 * 1 = 32 
	Sum of digits = 4 + 4 + 2 + 1 = 11 
	Result = 32 - 11 = 21
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.number:
		result = Solution().subtractProductAndSum(args.number[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()