# 2011. Final Value of Variable After Performing Operations


from colorama import Fore as F
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-o', '--operations', metavar='o', nargs=1, type=str, help='Operations')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def finalValueAfterOperations(self, operations: list) -> int:
        result = 0
        for el in operations:
            if '+' in el:
                result += 1
            else:
                result -= 1
        return result


def main():
	descr = f'''
{F.RED}============================================================================={F.RESET}
{F.GREEN}		
		# 2011. Final Value of Variable After Performing Operations

There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations,
 return the final value of X after performing all the operations.
{F.RESET}
{F.RED}============================================================================={F.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-2011.py -o "--X, X++, X++"
	>>> 1
{F.GREEN}
	Explanation: The operations are performed as follows:
	Initially, X = 0.
	--X: X is decremented by 1, X =  0 - 1 = -1.
	X++: X is incremented by 1, X = -1 + 1 =  0.
	X++: X is incremented by 1, X =  0 + 1 =  1.
{F.RESET}
Example 2:
	$ python3 l-2011.py -o "++X, ++X, X++"
	>>> 3
{F.GREEN}
	Explanation: The operations are performed as follows:
	Initially, X = 0.
	++X: X is incremented by 1, X = 0 + 1 = 1.
	++X: X is incremented by 1, X = 1 + 1 = 2.
	X++: X is incremented by 1, X = 2 + 1 = 3.
{F.RESET}
Example 3:
	$ python3 l-2011.py -o "X++, ++X, --X, X--"
	>>> 0
{F.GREEN}
	Explanation: The operations are performed as follows:
	Initially, X = 0.
	X++: X is incremented by 1, X = 0 + 1 = 1.
	++X: X is incremented by 1, X = 1 + 1 = 2.
	--X: X is decremented by 1, X = 2 - 1 = 1.
	X--: X is decremented by 1, X = 1 - 1 = 0.
{F.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.operations:
		op = args.operations[0].split(',')
		result = Solution().finalValueAfterOperations(op)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()