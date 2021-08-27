import argparse

def getArgs(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-arg', type=str, nargs='+', help='Argument')
    parser.add_argument('-d', nargs='*', help='Show description')
    parser.add_argument('-e', nargs='*', help='Show example how script is working')
    
    args = parser.parse_args()

    return args

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lst_r = []
        lst_m = []
        for letter in ransomNote:
            lst_r.append(letter)
        for letter in magazine:
            lst_m.append(letter)
        
        
        for el in lst_r:
            if el in lst_m:
                lst_m.remove(el)
            else:
                return False
        return True


def Main():
    descr = '''
Given two stings ransomNote and magazine, return true if 
ransomNote can be constructed from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
    '''

    examples = '''
Example 1:

    Input: "a",  "b"
    Output: false

Example 2:
    Input: "aa", "ab"
    Output: false

Example 3:
    Input: "aa", "aab"
    Output: true
    '''


    args = getArgs(descr)


    if args.d != None:
        print(descr)

    elif args.e != None:
        print(examples)

    elif args.arg != None:
        result = Solution().canConstruct(args.arg[0], args.arg[1])
        print(result)
if __name__ == '__main__':
    Main()