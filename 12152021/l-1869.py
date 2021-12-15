# 1869. Longer Contiguous Segments of Ones than Zeros

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--string', type=str, nargs=1, help='Binary string')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        lst_zeroes = s.split('1')
        lst_ones = s.split('0')
        
        z = []
        o = []
        
        for el in lst_zeroes:
            z.append(len(el))
        
        for el in lst_ones:
            o.append(len(el))
        
        return max(o) > max(z)


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 1869. Longer Contiguous Segments of Ones than Zeros

Given a binary string s, return true if the longest contiguous 
segment of 1's is strictly longer than the longest contiguous 
segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment 
of 1s has length 2, and the longest continuous segment of 0s has 
length 3.
Note that if there are no 0's, then the longest continuous segment 
of 0's is considered to have a length 0. The same applies if there 
is no 1's.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1869.py --string "1101"
	>>> True
{Fore.GREEN}
	Explanation:
	The longest contiguous segment of 1s has length 2: "1101"
	The longest contiguous segment of 0s has length 1: "1101"
	The segment of 1s is longer, so return true.
{Fore.RESET}
Example 2:
	$ python3 l-1869.py --string "111000"
	>>> False
{Fore.GREEN}
	Explanation:
	The longest contiguous segment of 1s has length 3: "111000"
	The longest contiguous segment of 0s has length 3: "111000"
	The segment of 1s is not longer, so return false.
{Fore.RESET}
Example 3:
	$ python3 l-1869.py --string "110100010"
	>>> False
{Fore.GREEN}
	Explanation:
	The longest contiguous segment of 1s has length 2: "110100010"
	The longest contiguous segment of 0s has length 3: "110100010"
	The segment of 1s is not longer, so return false.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().checkZeroOnes(args.string[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()

