import argparse

descr = '''
You are given a string s, return the number of segments in the string. 

A segment is defined to be a contiguous sequence of non-space characters.
'''

def BuildArgParser():
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-args', type=str, nargs=1, help='Arguments')
    parser.add_argument('-d', nargs='*', help='Show description')
    parser.add_argument('-e', nargs='*', help='Show example how script is working')
    return parser

class Solution:
    def countSegments(self, s: str) -> int:
        r = s.strip().split(' ')
        lst = []
        for index, el in enumerate(r):
            if el != '':
                lst.append(el)
        return len(lst)       

def Main():
    parser = BuildArgParser()
    args = parser.parse_args()

    if args.args != None:
        args_lst = args.args 
        for el in args_lst:
            result = Solution().countSegments(el)
            print(result)

    elif args.d != None:
        print(descr)

    elif args.e != None:
        print('Input: "Hello world"\nOutput: 2')

    else:
        parser.print_help()


if __name__=='__main__':
    Main()
