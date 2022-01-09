# 1041. Robot Bounded In Circle

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-i', '--instructions', type=str, nargs=1, help='Instructions')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


def findDirection(direction, l_or_r):
    lst = ['W', 'N', 'E', 'S']
    
    idx = lst.index(direction)
    
    if l_or_r == 'L':
        if idx > 0:
            direction = lst[idx-1]
        else:
            direction = lst[len(lst)-1]
        return direction
    else:
        if idx < len(lst) - 1:
            direction = lst[idx+1]
        else:
            direction = lst[0]
        return direction


    
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 'N'
        for el in instructions:
            if el in ['L', 'R']:
                direction = findDirection(direction, el)
            elif el == 'G':
                if direction == 'N':
                    y += 1
                elif direction == 'S':
                    y -= 1
                elif direction == 'W':
                    x -= 1
                elif direction == 'E':
                    x += 1
                    
        if x == 0 and y == 0:
            return True
        else:
            for i in range(4):
                for el in instructions:
                    if el in ['L', 'R']:
                        direction = findDirection(direction, el)
                    elif el == 'G':
                        if direction == 'N':
                            y += 1
                        elif direction == 'S':
                            y -= 1
                        elif direction == 'W':
                            x -= 1
                        elif direction == 'E':
                            x += 1
                if x == 0 and y == 0:
                    return True


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces
north. The robot can receive one of three instructions:
	 - "G": go straight 1 unit;
	 - "L": turn 90 degrees to the left;
	 - "R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them
forever.

Return true if and only if there exists a circle in the plane such
that the robot never leaves the circle.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1041.py --instructions "GGLLGG"
	>>> True
{Fore.GREEN}
	Explanation: 
		The robot moves from (0,0) to (0,2), turns 180 degrees, and
			then returns to (0,0).
		When repeating these instructions, the robot remains in the
			circle of radius 2 centered at the origin.
Example 2:
	$ python3 l-1041.py --instructions "GG"
	>>> False
{Fore.GREEN}
	Explanation:
		The robot moves north indefinitely.
{Fore.RESET}
Example 3:
	$ python3 l-1041.py --instructions "GL"
	>>> True
{Fore.GREEN}
	Explanation:
		The robot moves from (0, 0) -> (0, 1) -> (-1, 1) ->
			(-1, 0) -> (0, 0) -> ...
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.instructions:
		result = Solution().isRobotBounded(args.instructions[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
	