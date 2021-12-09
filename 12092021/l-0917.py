# 917. Reverse Only Letters

import argparse
from colorama import Fore 


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', '--string', type=str, nargs=1, help='String')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Get list of letters from string
        mask = []
        letters = []
        
        for el in s:
            # If letter
            if el.isalpha():
                mask.append(None)
                letters.append(el)
            else:
                mask.append(el)
        
        # Reverse letters list
        letters = letters[::-1]
        
        # Put letters back
        for index, el in enumerate(mask):
            if el == None:
                mask[index] = letters[0]
                letters.remove(letters[0])
        
        # Build result
        result = (''.join(mask))
        return result


def main():
	descr = f'''
{Fore.RED}==============================================================================={Fore.RESET}
{Fore.GREEN}
	# 917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
{Fore.RESET}	
{Fore.RED}==============================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0917.py --string "ab-cd"
	>>> "dc-ba"

Example 2:
	$ python3 l-0917.py --string "a-bC-dEf-ghIj"
	>>> "j-Ih-gfE-dCba"

Example 3:
	$ python3 l-0917.py --string "Test1ng-Leet=code-Q!"
	>>> "Qedo1ct-eeLg=ntse-T!"
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().reverseOnlyLetters(args.string[0])
		print(f'"{result}"')

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()