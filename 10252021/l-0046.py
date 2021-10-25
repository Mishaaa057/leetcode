# 46. Permutations
# Difficulry - [Medium]


import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Numbers array')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


# Еhe function goes through each item in the list and swaps with other items and then creates new lists with
def my_fun(lst, s_lst=[]):
    new_lst = []
    for index1, el1 in enumerate(lst):
        temp = lst.copy()
        for index2, el2 in enumerate(lst):
            temp = lst.copy()
            if el1 != el2:
                temp[index1], temp[index2] = temp[index2], temp[index1]
                if temp not in new_lst and temp not in s_lst:
                    new_lst.append(temp)
    return new_lst
                

class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        
        new_lst = (my_fun(nums))
        for el in new_lst:
            new_lst += my_fun(el, new_lst)
        return new_lst


def main():
	descr = f'''
{Fore.RED}==============================================={Fore.RESET}
{Fore.GREEN}
	# 46. Permutations

Given an array nums of distinct integers, 
return all the possible permutations. 
You can return the answer in any order.
{Fore.RESET}
{Fore.RED}==============================================={Fore.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0046.py --nums 1 2 3
	>>> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
	$ python3 l-0046.py --nums 0 1
	>>> [[0,1],[1,0]]

Example 3:
	$ python3 l-0046.py --nums 1
	>>> [[1]]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().permute(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()	


if __name__=='__main__':
	main()