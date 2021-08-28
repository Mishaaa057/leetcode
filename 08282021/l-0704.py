import argparse

def getArgs(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('--list', '-l', type=int, nargs='+', help='Arguments')
    parser.add_argument('--target', '-t',type=int, nargs=1, help='Target')
    parser.add_argument('-d',  nargs='*', help='Description')
    parser.add_argument('-e', nargs='*', help='Example')

    return parser

class Solution:
    def search(self, nums:list, target: int) -> int:
        if target in nums:
            for index, el in enumerate(nums):
                if  el == target:
                    return index
        return -1

def Main():
    descr = '''
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. If target exists, 
then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
    '''

    example = '''
Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
    '''

    parser = getArgs(descr)
    args = parser.parse_args()
    
    if args.d != None:
        print(descr)

    elif args.e != None:
        print(example) 

    elif args.list != None and args.target != None:
        print(args.list, args.target)
        print(Solution().search(args.list, args.target[0]))

    else:
        parser.print_help()


if __name__ == '__main__':
    Main()
