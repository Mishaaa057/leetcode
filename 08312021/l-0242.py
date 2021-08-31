import argparse

def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-s', type=str, nargs=1, help='First string')
	parser.add_argument('-t', type=str, nargs=1, help='Second string')
	parser.add_argument('-d', nargs='*', help='Description')
	parser.add_argument('-e', nargs='*', help='Example')

	return parser 


def build_lst(string):
    lst = []
    for el in string:
        lst.append(el)
    return lst


class Solution:
    def isAnagram(self, s: str, t: str):
        lst_s = build_lst(s)
        lst_t = build_lst(t)
        
        if len(lst_s) == len(lst_t):
            for index, el in enumerate(lst_s):
                if el in lst_t:
                    lst_t.remove(el)
                elif el not in lst_t:
                    return False
            return True
        else:
        	return False
                

def Main():
	descr = '''
Given two strings s and t, 
return true if t is an anagram of s, and false otherwise.
	'''

	example = '''
Example 1:
	Input: s = "anagram", t = "nagaram"
	Output: true

Example 2:
	Input: s = "rat", t = "car"
	Output: false
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.s != None and args.t != None:
		result = Solution().isAnagram(args.s[0], args.t[0])
		print(result)

	elif args.d != None:
		print(descr)

	elif args.e != None:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()
