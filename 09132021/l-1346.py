# 1346. Check If N and Its Double Exist


from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--array', '-arr', type=int, 
		nargs='+', metavar='num', help='Array of integers')
	parser.add_argument('--description', '-d',
		action='store_true', help='Show description')
	parser.add_argument('--example', '-e', 
		action='store_true', help='Show some examples')

	return parser 


class Solution:
    def checkIfExist(self, arr):
        
        for index1, num1 in  enumerate(arr):
            for index2, num2 in enumerate(arr):
                if index1 != index2:
                    if num1 == num2 * 2:
                        return True
        
        return False


def Main():
	descr = f'''
{Fore.RED}============================================================={Fore.RESET}
		{Fore.GREEN}# 1346. Check If N and Its Double Exist

	Given an array arr of integers, check if there
	exists two integers N and M such that N is the double
	of M ( i.e. N = 2 * M).

	More formally check if there exists 
	two indices i and j such that :
		i != j
		0 <= i, j < arr.length
		arr[i] == 2 * arr[j]{Fore.RESET}
		
{Fore.RED}============================================================={Fore.RESET}
	'''

	example = '''
Example 1:
	
	$ python3 --array  10 2 5 3
	>>> true

	Explanation: N = 10 is the double of M = 5,
	that is, 10 = 2 * 5.

Example 2:

	$ python3 --array 7 1 14 11
	>>> true
	
	Explanation: N = 14 is the double of M = 7,
	that is, 14 = 2 * 7.

Example 3:

	$ python3 --array 3 1 7 11
	>>> false
	Explanation: In this case does not exist N and M,
	such that N = 2 * M.
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.array:
		result = Solution().checkIfExist(args.array)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()



if __name__ == '__main__':
	Main()