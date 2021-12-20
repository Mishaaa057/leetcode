# 228. Summary Ranges

import argparse
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', '--nums', type=int, nargs='+', help='Array of integers')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def summaryRanges(self, nums: list) -> list:
        ranges = []
        range_ = [None, None]
        
        for index, el in enumerate(nums):
            if index > 0:
                if nums[index - 1] + 1 == el:
                    range_[1] = el
                    if index+1 == len(nums):
                        ranges.append(range_)
                else:
                    ranges.append(range_.copy())
                    range_[0] = el
                    range_[1] = None
                    if index+1 == len(nums):
                        ranges.append(range_)
            else:
                range_[0] = el
                if index+1 == len(nums):
                    ranges.append(range_)
        
        result = []    
        for ran in ranges:
            if ran[1]:
                result.append(f'{ran[0]}->{ran[1]}')
            else:
                result.append(str(ran[0]))
        
        return result


def main():
	descr = f'''
{Fore.RED}{'=' * 75}{Fore.RESET}
{Fore.GREEN}
	# 228. Summary Ranges

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers
in the array exactly. That is, each element of nums is covered by
exactly one of the ranges, and there is no integer x such that x is
in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
	"a->b" if a != b
	"a" if a == b
{Fore.RESET}
{Fore.RED}{'=' * 75}{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0228.py --nums 0 1 2 4 5 7
	Output: ["0->2","4->5","7"]
{Fore.GREEN}
	Explanation: The ranges are:
		[0,2] --> "0->2"
		[4,5] --> "4->5"
		[7,7] --> "7"
{Fore.RESET}
Example 2:
	$ python3 l-0228.py --nums 0 2 3 4 6 8 9
	Output: ["0","2->4","6","8->9"]
{Fore.GREEN}
	Explanation: The ranges are:
		[0,0] --> "0"
		[2,4] --> "2->4"
		[6,6] --> "6"
		[8,9] --> "8->9"
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.nums:
		result = Solution().summaryRanges(args.nums)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()