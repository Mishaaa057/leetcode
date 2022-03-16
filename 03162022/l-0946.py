# 946. Validate Stack Sequences

import argparse
from sre_parse import expand_template
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('--pushed', type=int, nargs="+",
        help='Pushed array')
    parser.add_argument('--popped', type=int, nargs="+",
        help='Pushed popped')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        stack = []
        
        i = 0
        
        for el in pushed:
            stack.append(el)
            
            while stack and stack[-1] == popped[i]:
                if i < len(popped):
                    stack.pop(len(stack)-1)
                    i += 1
            
        return stack == []


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 946. Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values,
return true if this could have been the result of a sequence of push
and pop operations on an initially empty stack, or false otherwise.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0946.py --pushed 1 2 3 4 5 --popped 4 5 3 2 1
    >>> True
{Fore.GREEN}
    Explanation: We might do the following sequence:
    push(1), push(2), push(3), push(4),
    pop() -> 4,
    push(5),
    pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
{Fore.RESET}
Example 2:
    $ python3 l-0946.py --pushed 1 2 3 4 5  --popped 4 3 5 2 1
    >>> False
{Fore.GREEN}
    Explanation: 1 cannot be popped before 2.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.pushed and args.popped:
        result = Solution().validateStackSequences(args.pushed, args.popped)
        print(result)
    
    elif args.description:
        print(descr)

    elif args.example:
        print(example)
    
    else:
        parser.print_help()
    

if __name__=='__main__':
    main()
    