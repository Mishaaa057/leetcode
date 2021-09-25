# 344. Reverse String
# Difficulty - [Easy]


# 1137. N-th Tribonacci Number


from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--string', '-s', metavar='s', nargs='+', type=str, help='Array of characters')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def reverseString(self, s: list) -> None:
        s2 = []
        i = len(s) - 1
        while i >= 0:
            s2.append(s[i])
            i -= 1
        for index, el in enumerate(s2):
            s[index] = el
            '''
			На літ коді не потрібно нічого повертати,
			але тут чисто щоб виводило результат 
            '''
        return s


def main():
	descr = f'''
{Fore.RED}================================================================={Fore.RESET}
	{Fore.GREEN}# 344. Reverse String

Write a function that reverses a string. 
The input string is given as an array of characters s.{Fore.RESET}
{Fore.RED}================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0344.py --string h e l l o
	>>> ["o","l","l","e","h"]

Example 2:
	$ python3 l-0344.py --string H a n n a h
	>>> ["h","a","n","n","a","H"]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.string:
		result = Solution().reverseString(args.string)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()