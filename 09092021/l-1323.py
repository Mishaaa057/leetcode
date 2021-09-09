# 1323. Maximum 69 Number


import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--num', '-n', type=int, nargs=1, help='Positive integer')
	parser.add_argument('-d', nargs='*', help='Show description')
	parser.add_argument('-e', nargs='*', help='Show Examples')

	return parser


class Solution:
    def maximum69Number(self, num):
        
        lever = False
        result = ''
        
        for el in str(num):
            if lever != True:
                if el != '6':
                    result += el
                if el == '6':
                    result += '9'
                    lever = True
            else:
                result += el
        
        return result
                

def Main():
	descr = '''
Given a positive integer num consisting only
of digits 6 and 9.

Return the maximum number you can get by
changing at most one digit (6 becomes 9, and 9 becomes 6).
	'''

	example = '''
Example 1:
	Input: num = 9669
	Output: 9969
	Explanation: 
	Changing the first digit results in 6669.
	Changing the second digit results in 9969.
	Changing the third digit results in 9699.
	Changing the fourth digit results in 9666. 
	The maximum number is 9969.

Example 2:
	Input: num = 9996
	Output: 9999
	Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
	Input: num = 9999
	Output: 9999
	Explanation: It is better not to apply any change.
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.num != None:
		result = Solution().maximum69Number(args.num[0])
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()


if __name__ == '__main__':
	Main()