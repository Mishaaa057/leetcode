# 1812. Determine Color of a Chessboard Square


import argparse
import string
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-c', '--coordinates', type=str, nargs=1, help='Coordinates')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letters = (string.ascii_lowercase)[:8]
        
        letter_idx = letters.index(coordinates[0])
        
        a = (letter_idx + 1) % 2 == 0
        b = (int(coordinates[1]) % 2) == 0
                
        if a == b and a == True:
            return False 
        
        elif a == b and a == False:
            
            return False
        else:
            return True


def main():
	descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
	# 1812. Determine Color of a Chessboard Square

You are given coordinates, a string that represents the coordinates
of a square of the chessboard. Below is a chessboard for your
reference.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1812.py --coordinates "a1"
	>>> False
{Fore.GREEN}
	Explanation: From the chessboard above, the square with
		coordinates "a1" is black, so return false.
{Fore.RESET}
Example 2:
	$ python3 l-1812.py --coordinates "h3"
	>>> True
{Fore.GREEN}
	Explanation: From the chessboard above, the square with
		coordinates "h3" is white, so return true.
{Fore.RESET}
Example 3:
	$ python3 l-1812.py --coordinates "c7"
	>>> False
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.coordinates:
		result = Solution().squareIsWhite(args.coordinates[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
