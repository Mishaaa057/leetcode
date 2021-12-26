# 973. K Closest Points to Origin

import argparse
from colorama import Fore
from math import sqrt


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-p', '--points', type=str, nargs=1,
		metavar='[[x1,y1],[x2,y2]]', help='Array of points (input as string)')
	parser.add_argument('-k', type=int, nargs=1, help='Integer K')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def kClosest(self, points: list, k: int) -> list:
        dct = {}   # {[x, y]:2}
        for point in points:
            # Find distance
            x = point[0]
            y = point[1]
            dist = sqrt(x**2 + y**2)
            
            if dist not in dct:
                dct[dist] = [point]
            else:
                dct[dist].append(point)
        
        result = []
        for key in sorted(dct):
            if len(result) != k:
                if len(dct[key]) > 1:
                    for el in dct[key]:
                        result.append(el)
                    
                else:
                    result.append(dct[key][0])
            
                if len(result) == k:
                    return result


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a
point on the X-Y plane and an integer k, return the k closest points
to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean
distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to
be unique (except for the order that it is in).
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0973.py --points "[[1,3],[-2,2]]" -k 1
	>>> [[-2,2]]
{Fore.GREEN}
	Explanation:
		The distance between (1, 3) and the origin is sqrt(10).
		The distance between (-2, 2) and the origin is sqrt(8).
		Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
		We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
{Fore.RESET}
Example 2:
	$ python3 l-0973.py --points "[[3,3],[5,-1],[-2,4]]" -k 2
	>>> [[3,3],[-2,4]]
{Fore.GREEN}
	Explanation:
		The answer [[-2,4],[3,3]] would also be accepted.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.points and args.k:
		points = eval(args.points[0])
		result = Solution().kClosest(points, args.k[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
