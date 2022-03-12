# 2169. Count Operations to Obtain Zero

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n1', '--num1', type=int, nargs=1,
        help='Integer 1')
    parser.add_argument('-n2', '--num2', type=int, nargs=1,
        help='Integer 2')
    
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        
        while True:
            if num1 == num2 and num1 == 0 or (num1 == 0 or num2 == 0):
                return counter
            
            if num1 > num2:
                num1 = num1 - num2
                
            elif num1 < num2:
                num2 = num2 - num1
                
            else:
                return counter + 1
            
            counter += 1


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 2169. Count Operations to Obtain Zero

You are given two non-negative integers num1 and num2.

In one operation, if num1 >= num2, you must subtract num2 from num1,
otherwise subtract num1 from num2.

For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus
obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5,
after one operation, num1 = 4 and num2 = 1.
Return the number of operations required to make either num1 = 0 or
num2 = 0.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-2169.py --num1 2 --num2 3
    >>> 3
{Fore.GREEN}
    Explanation: 
        - Operation 1: num1 = 2, num2 = 3. Since num1 < num2,
        we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
        - Operation 2: num1 = 2, num2 = 1. Since num1 > num2,
        we subtract num2 from num1.
        - Operation 3: num1 = 1, num2 = 1. Since num1 == num2,
        we subtract num2 from num1.
        Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need
        to perform any further operations.
    So the total number of operations required is 3.
{Fore.RESET}
Example 2:
    $ python3 l-2169.py --num1 10 --num2 10
    >>> 1
{Fore.GREEN}
    Explanation: 
        - Operation 1: num1 = 10, num2 = 10. Since num1 == num2,
            we subtract num2 from num1 and get num1 = 10 - 10 = 0.
            Now num1 = 0 and num2 = 10. Since num1 == 0, we are done.
        So the total number of operations required is 1.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.num1 and args.num2:
        result = Solution().countOperations(args.num1[0], args.num2[0])
        print(result)

    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
