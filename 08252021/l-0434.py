import argparse

descr = '''
You are given a string s, return the number of segments in the string. 

A segment is defined to be a contiguous sequence of non-space characters.
'''

parser = argparse.ArgumentParser(descr)
parser.add_argument('-args', type=str, nargs='+', help='Arguments')
parser.add_argument('-d', nargs='?', help='Show description')
parser.add_argument('-e', nargs='?', help='Show example how script is working')
args = parser.parse_args()

class Solution:
    def countSegments(self, s: str) -> int:
        r = s.strip().split(' ')
        lst = []
        for index, el in enumerate(r):
            if el != '':
                lst.append(el)
        return len(lst)       

def Main():
    if args.args != None:
        args_lst = args.args 
        for el in args_lst:
            result = Solution().countSegments(el)
            print(result)

    if args.d != None:
        print(descr)

    if args.e != None:
        print('Input: "Hello world"\nOutput: 2')


if __name__=='__main__':
    Main()