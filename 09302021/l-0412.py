# 412. Fizz Buzz


from colorama import Fore as F
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-n', metavar='n', nargs=1, type=int, help='Integer n')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


class Solution:
    def fizzBuzz(self, n: int) -> list:
        result = []
        for i in range(n):
            i = i+1
            
            if i%3 == 0 and i%5 == 0:
                i = 'FizzBuzz'
            
            elif i%3 == 0:
                i = 'Fizz'
            
            elif i%5 == 0:
                i = 'Buzz'
            
            result.append(str(i))
        return result


def main():
	descr = f'''
{F.RED}=========================================================={F.RESET}
{F.GREEN}		
		# 412. Fizz Buzzd

Given an integer n, return a string array 
answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
{F.RESET}
{F.RED}=========================================================={F.RESET}
	'''

	example = '''
Example 1:
	$ python3 l-0412.py -n 3
	>>> ["1","2","Fizz"]

Example 2:
	$ python3 l-0412.py -n 5
	>>> ["1","2","Fizz","4","Buzz"]

Example 3:
	$ python3 l-0412.py -n 15
	>>> ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz",
		"Buzz","11","Fizz","13","14","FizzBuzz"]
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.n:
		result = Solution().fizzBuzz(args.n[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()