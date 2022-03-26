# 1678. Goal Parser Interpretation

import argparse
from tkinter import E
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)

    parser.add_argument('-c', '--command', type=str, nargs=1,
        help='Command')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def interpret(self, command: str) -> str:
        
        command = list(command)
        
        for idx, el in enumerate(command):   
            if el == '(':
                if idx + 1 < len(command):
                    if command[idx+1] == ')':
                        command.pop(idx+1)
                        command.pop(idx)
                        command.insert(idx, 'o')
                        continue

                command.pop(idx)
                
        while ')' in command:
            command.remove(')')
        
        return ''.join(command)


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 1678. Goal Parser Interpretation

You own a Goal Parser that can interpret a string command. The
command consists of an alphabet of "G", "()" and/or "(al)" in
some order. The Goal Parser will interpret "G" as the string "G",
"()" as the string "o", and "(al)" as the string "al". The
interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation
of command.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1678.py --command "G()(al)"
    >>> "Goal"
{Fore.GREEN}
    Explanation:
    The Goal Parser interprets the command as follows:
        G -> G
        () -> o
        (al) -> al
    The final concatenated result is "Goal".
{Fore.RESET}
Example 2:
    $ python3 l-1678.py --command "G()()()()(al)"
    >>> "Gooooal"

Example 3:
    $ python3 l-1678.py --command "(al)G(al)()()G"
    >>> "alGalooG"
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.command:
        result = Solution().interpret(args.command[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
