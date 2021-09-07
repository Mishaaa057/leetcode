# 1662. Check If Two String Arrays are Equivalent

import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--word1', type=str, nargs='+', help='Array 1')
	parser.add_argument('--word2', type=str, nargs='+', help='Array 2')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        string1 = ''
        string2 = ''
        
        for el in word1:
            string1 += el
            
        for el in word2:
            string2 += el
        
        return string1 == string2
        


def Main():
	descr ='''
Given two string arrays word1 and word2, return true if 
the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements
concatenated in order forms the string.
	'''

	example = '''
Example 1:
	Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
	Output: true
	Explanation:
	word1 represents string "ab" + "c" -> "abc"
	word2 represents string "a" + "bc" -> "abc"
	The strings are the same, so return true.

Example 2:
	Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
	Output: false

Example 3:
	Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
	Output: true
	'''
	

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.word1 != None and args.word2 != None:
		result = Solution().arrayStringsAreEqual(args.word1, args.word2)
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()

if __name__ == '__main__':
	Main()	