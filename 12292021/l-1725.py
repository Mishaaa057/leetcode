# 1725. Number Of Rectangles That Can Form The Largest Square

import argparse
from colorama import Fore
from math import sqrt


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-r', '--rectangles', type=str, nargs=1,
		metavar='[[l1,w1],[l2,w2]]', help='Array of rectangles (input as string)')
	parser.add_argument('-k', type=int, nargs=1, help='Integer K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def countGoodRectangles(self, rectangles: list) -> int:
        lst = []
        for el in rectangles:
            lst.append(min(el))
        
        n = max(lst)
        return lst.count(n)


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 1725. Number Of Rectangles That Can Form The Largest Square

You are given an array rectangles where rectangles[i] = [li, wi]
represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length
of k if both k <= li and k <= wi. For example, if you have a
rectangle [4,6], you can cut it to get a square with a side length
of at most 4.

Let maxLen be the side length of the largest square you can obtain
from any of the given rectangles.

Return the number of rectangles that can make a square with a side
length of maxLen.
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1725.py --rectangles "[[5,8],[3,9],[5,12],[16,5]]"
	>>> 3
{Fore.GREEN}
	Explanation: The largest squares you can get from each rectangle
		are of lengths [5,3,5,5].
		The largest possible square is of length 5, and you can get it
		out of 3 rectangles.
{Fore.RESET}
Example 2:
	$ python3 l-1725.py --rectangles "[[2,3],[3,7],[4,3],[3,7]]"
	>>> 3
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.rectangles:
		rectangles = eval(args.rectangles[0])
		result = Solution().countGoodRectangles(rectangles)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
