# 1805. Number of Different Integers in a String

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-w', '--word', type=str, nargs=1, help='Some word')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Get list with numbers from word 
        nums = []
        num = ''
        for index, el in enumerate(word):
            
            try:
                el = int(el)
                num += str(el)
                
                if index == len(word)-1:
                    nums.append(num)
            except:
                if num != '':
                    nums.append(num)
                    num = ''
        
        # Converte numbers from string to integers 
        for index, el in enumerate(nums):
            nums[index] = int(el)
        
        # Remove dublicates from list
        result_nums = []
        for el in nums:
            if el not in result_nums:
                result_nums.append(el)
        
        return len(result_nums)


def main():
	descr = f'''
{Fore.RED}==========================================================================={Fore.RESET}
{Fore.GREEN}
	# 1805. Number of Different Integers in a String

You are given a string word that consists of digits and lowercase 
English letters.

You will replace every non-digit character with a space. For example, 
"a123bc34d8ef34" will become " 123  34 8  34". Notice that you are 
left with some integers that are separated by at least 
one space: "123", "34", "8", and "34".

Return the number of different integers after 
performing the replacement operations on word.

Two integers are considered different if their decimal representations 
without any leading zeros are different.
{Fore.RED}==========================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1805.py --word "a123bc34d8ef34"
	>>> 3
{Fore.GREEN}
	Explanation: The three different integers are "123", "34", 
	and "8". Notice that "34" is only counted once.
{Fore.RESET}
Example 2:
	$ python3 l-1805.py --word "leet1234code234"
	>>> 2

Example 3:
	$ python3 l-1805.py --word "a1b01c001"
	>>> 1
{Fore.GREEN}
	Explanation: The three integers "1", "01", and "001" all represent the same integer because
	the leading zeros are ignored when comparing their decimal values.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.word:
		result = Solution().numDifferentIntegers(args.word[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()
	