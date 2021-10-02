# 1431. Kids With the Greatest Number of Candies


from colorama import Fore as F
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-c','--candies', metavar='n', nargs='+', type=int, help='Candies integer array')
	parser.add_argument('-ec','--extracandies', metavar='n', nargs='+', type=int, help=' Extra candies integer array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        result = []
        for el in candies:
            if el + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result


def main():
	descr = f'''
{F.RED}=========================================================================={F.RESET}
{F.GREEN}		
		# 1431. Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, denoting the number of extra candies that 
you have.

Return a boolean array result of length n, where result[i] is true if, 
after giving the ith kid all the extraCandies, they will have the greatest 
number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
{F.RESET}
{F.RED}=========================================================================={F.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-1431.py --candies 2 3 5 1 3 --extracandies 3
	>>> [true,true,true,false,true] 

Example 2:
	$ python3 l-1431.py --candies 4 2 1 1 2 --extracandies 1
	>>> [true,false,false,false,false] 

Example 3:
	$ python3 l-1431.py --candies 12 1 12  --extracandies 10
	>>> [true,false,true]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.candies and args.extracandies:
		result = Solution().kidsWithCandies(args.candies, args.extracandies[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()