import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--jewels', '-j', nargs=1, type=str, help='Jewels [str]')
	parser.add_argument('--stones', '-s', nargs=1, type=str, help='Stones [str]')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')
	
	return parser


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for s in stones:
            if s in jewels:
                counter += 1
        return counter


def Main():
	descr = '''
You're given strings jewels representing the types of stones that are jewels, and stones
representing the stones you have. Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''

	example = '''
Example 1:
	Input: -j "aA" -s "aAAbbbb"
	Output: 3

Example 2:
	Input: --jewels "z" --stones "ZZ"
	Output: 0
'''
	
	parser = BuildArgParser(descr)
	args = parser.parse_args()


	if args.jewels != None and args.stones != None:
		result = Solution().numJewelsInStones(args.jewels[0], args.stones[0])
		print(result)		

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()

if __name__=='__main__':
	Main()