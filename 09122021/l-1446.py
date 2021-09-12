# 1446. Consecutive Characters

from colorama import Fore
import argparse


def BuildArgParser(descr):

	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--string', '-s', type=str, nargs=1,
		metavar='string', help = 'Provide a string')
	parser.add_argument('--description', '-d', 
		action = 'store_true', help = 'Show description')
	parser.add_argument('--example', '-e', 
		action = 'store_true', help='Show examples')

	return parser 



class Solution:
    def maxPower(self, s: str) -> int:
        lst = []
        
        counter = 1
        for index, el in enumerate(s):
            if index > 0:
                if el == s[index - 1]:
                    counter += 1
                    if index == len(s) - 1:
                        lst.append(counter)
                else:
                    lst.append(counter)
                    counter = 1 
            else:
                lst.append(counter)
        

        return max(lst)



def Main():
	descr = f'''
{Fore.GREEN}	#446. Consecutive Characters
The power of the string is the maximum length of 
a non-empty substring that contains only one unique 
character.

Given a string s, return the power of s.
{Fore.RESET}
	'''

	example='''
Example 1:
	$ python3 --string "leetcode"
	>>> 2
	
	Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
	$ python3 --string "abbcccddddeeeeedcba"
	>>> 5
	
	Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
	$ python3 --sring "triplepillooooow"
	>>> 5

Example 4:
	$ python3 -s "hooraaaaaaaaaaay"
	>>> 11

Example 5:
	$ python3 -s "tourist"
	>>> 1
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().maxPower(args.string[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__ == '__main__':
	Main()

