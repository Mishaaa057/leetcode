# 217. Contains Duplicate


from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-arr', '--array', type=int, metavar='n',
		nargs='+', help='Integer array')
	parser.add_argument('-d', '--description', action='store_true',
		help='Show description')
	parser.add_argument('-e', '--example', action='store_true',
		help='Show example')

	return parser 


class Solution:
    def containsDuplicate(self, nums: list) -> bool:        
        
        dct = {}
        
        for el in nums:
            if el in dct:
                return True
            else:
                dct[el] = 1
        return False
        


def Main():
	descr = f'''
{Fore.RED}============================================================================={Fore.RESET}
		
		{Fore.GREEN}# 217. Contains Duplicate

	Given an integer array nums, return true if any value
	appears at least twice in the array, and return false if 
	every element is distinct.{Fore.RESET}
{Fore.RED}============================================================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0217.py --arr 1 2 3 1
	>>> true

Example 2:
	$ python3 l-0217.py --arr 1 2 3 4
	>>> false

Example 3:

	$ python3 l-0217.py --arr 1 1 1 3 3 4 3 2 4 2
	>>> true
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.array:
		result = Solution().containsDuplicate(args.array)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()
