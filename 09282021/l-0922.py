# 922. Sort Array By Parity II


from colorama import Fore as F
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', metavar='n', nargs='+', type=int, help='Array of integers')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def sortArrayByParityII(self, nums: list) -> list:
        odd = [] # [4, 2]
        even = [] # [7, 5]
        
        # sort odd and even numbers
        for num in nums:
            if num % 2 == 0:
                odd.append(num)
            else:
                even.append(num)
        
        # create result array from odd and even numbers
        result = [] # [odd, even, odd, even, ...]
        for index, num in enumerate(odd):
            result.append(num)
            result.append(even[index])
        
        return result


def main():
	descr = f'''
{F.RED}=========================================================={F.RESET}
{F.GREEN}
	# 922. Sort Array By Parity II

Given an array of integers nums, half of the 
integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, 
i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.
{F.RESET}
{F.RED}=========================================================={F.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0922.py --nums 4 2 5 7 
	>>> [4,5,2,7]
{F.GREEN}
	Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] 
	would also have been accepted.
{F.RESET}
Example 2:
	$ python3 l-0922.py --nums 2 3
	>>> [2,3]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().sortArrayByParityII(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()