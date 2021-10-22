# 451. Sort Characters By Frequency
# Difficulty - [Medium]

import argparse 
from colorama import Fore

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--string',nargs=1, type=str, help='String')
	parser.add_argument('-d', '--description', action='store_true', help='Show description') 
	parser.add_argument('-e', '--example', action='store_true', help='Show example') 
	
	return parser


class Solution:
    def frequencySort(self, s: str) -> str:
        # Write Dictionary
        dct = {}
        for el in s:
            if el not in dct:
                dct[el] = 1
            else:
                dct[el] += 1

        # Get values list and keys list from dictionary
        values_list = list(dct.values())
        keys_list = list(dct.keys())
        
        # Generate Result string
        string = ''
        while len(values_list) > 0:
            max_index = values_list.index(max(values_list)) # Get index of max value
            string += (keys_list[max_index]) * max(values_list) # Add letter max_value times to string  
            
            values_list.remove(values_list[max_index]) # Remove elements thats already in string
            keys_list.remove(keys_list[max_index])
                    
                      # When the values list is [] 
        return string # return our result string


def main():
	descr = f'''
{Fore.RED}================================================{Fore.RESET}
{Fore.GREEN}
	# 451. Sort Characters By Frequency

Given a string s, sort it in decreasing order 
based on the frequency of the characters. The 
frequency of a character is the number of times 
it appears in the string.

Return the sorted string. If there are multiple 
answers, return any of them.
{Fore.RESET}
{Fore.RED}================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0451.py --string "tree"
	>>> "eert"
{Fore.GREEN}
	Explanation: 'e' appears twice while 'r' and 't' both appear once.
	So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
{Fore.RESET}
Example 2:
	$ python3 l-0451.py --string "cccaaa"
	>>> "aaaccc"
{Fore.GREEN}
	Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
	Note that "cacaca" is incorrect, as the same characters must be together.
{Fore.RESET}
Example 3:
	$ python3 l-0451.py --string "Aabb"
	>>> "bbAa"
{Fore.GREEN}
	Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
	Note that 'A' and 'a' are treated as two different characters.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().frequencySort(args.string[0])
		print(f'"{result}"')

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()

