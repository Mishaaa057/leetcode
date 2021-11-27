# 657. Robot Return to Origin

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-m', '--moves', type=str, nargs=1, help='String Moves')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dct = {}
        for el in moves:
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1
        
        
        
        if 'U' in dct or 'D' in dct:
            if 'U' in dct and 'D' in dct:
                if dct['U'] != dct['D']:
                    return False
            else:
                return False
        
        if 'L' in dct or 'R' in dct:
            if 'L' in dct and 'R' in dct:
                if dct['L'] != dct['R']:
                    return False
            else:
                return False
        
        return True
                

def main():
	descr = f'''
{Fore.RED}==========================================================================={Fore.RESET}
{Fore.GREEN}
	# 657. Robot Return to Origin

There is a robot starting at the position (0, 0), the origin, on a 2D 
plane. Given a sequence of its moves, judge if this robot ends up at 
(0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the 
robot where moves[i] represents its ith move. Valid moves are 'R' 
(right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all 
of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will 
always make the robot move to the right once, 'L' will always make it 
move left, etc. Also, assume that the magnitude of the robot's movement
is the same for each move.
{Fore.RESET}
{Fore.RED}==========================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0657.py --moves "UD"
	>>> True
{Fore.GREEN}
	Explanation: The robot moves up once, and then down once. 
	All moves have the same magnitude, so it ended up at the 
	origin where it started. Therefore, we return true.
{Fore.RESET}
Example 2:
	$ python3 l-0657.py --moves "LL"
	>>> False
{Fore.GREEN}
	Explanation: The robot moves left twice. It ends up two 
	"moves" to the left of the origin. We return false because 
	it is not at the origin at the end of its moves.
{Fore.RESET}
Example 3:
	$ python3 l-0657.py --moves "RRDD"
	>>> False

Example 4:
	$ python3 l-0657.py --moves "LDRRLRUULR"
	>>> False
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.moves:
		result = Solution().judgeCircle(args.moves[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()