# 485. Max Consecutive Ones


from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--nums', '-n', type=int, metavar='n',
		nargs='+', help='Integer array')
	parser.add_argument('--description', '-d', action='store_true',
		help='Show description')
	parser.add_argument('--example', '-e', action='store_true',
		help='Show example')

	return parser 


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        
        lst = []
        
        temp = 0
        for index, el in enumerate(nums):
            
            if el == 1:
                temp += 1
                if index + 1 == len(nums):
                    lst.append(temp)
            else:
                lst.append(temp)
                temp = 0

        return max(lst)


def Main():
	descr = f'''
{Fore.RED}==================================================={Fore.RESET}
	{Fore.GREEN}# 485. Max Consecutive Ones

Given a binary array nums, return the 
maximum number of consecutive 1's in the array.{Fore.RESET}
{Fore.RED}==================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0485.py --nums 1 1 0 1 1 1
	>>> 3
	{Fore.GREEN}
	Explanation: The first two digits or the last three 
	digits are consecutive 1s. The maximum number of consecutive 1s is 3.{Fore.RESET}

Example 2:
	$ python3 l-0485.py --nums 1 0 1 1 0 1
	>>> 2
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().findMaxConsecutiveOnes(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()
