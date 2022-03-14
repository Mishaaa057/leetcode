# 71. Simplify Path

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-p', '--path', type=str, nargs=1,
        help='String path')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        
        while '' in lst:
            lst.remove('')
        
        idx = 0
        
        while idx <= len(lst)-1:
            el = lst[idx]
            
            if el == '.':
                lst.pop(idx)
                idx -= 1
            elif el == '..':
                if idx >= 1:
                    lst.pop(idx-1)
                    lst.pop(idx-1)
                    
                    idx -= 2
                else:
                    lst.pop(idx)
                    idx -= 1
            
            idx += 1
        
        result = ''
        for el in lst:
            result += '/' + el
        
        if result == '':
            result = '/'
        
        return result


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 71. Simplify Path

Given a string path, which is an absolute path (starting with a slash
'/') to a file or directory in a Unix-style file system, convert it to
the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current
directory, a double period '..' refers to the directory up a level,
and any multiple consecutive slashes (i.e. '//') are treated as a
single slash '/'. For this problem, any other format of periods such
as '...' are treated as file/directory names.

The canonical path should have the following format:
    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root
    directory to the target file or directory (i.e., no period '.' or
    double period '..')
    Return the simplified canonical path.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0071.py --path "/home/"
    >>> "/home"
{Fore.GREEN}
    Explanation:
        Note that there is no trailing slash after the last directory name.
{Fore.RESET}
Example 2:
    $ python3 l-0071.py --path "/../"
    >>> "/"
{Fore.GREEN}
    Explanation:
        Going one level up from the root directory is a no-op, as the
        root level is the highest level you can go.
{Fore.RESET}
Example 3:
    $ python3 l-0071.py --path "/home//foo/"
    >>> "/home/foo"
{Fore.GREEN}
    Explanation:
        In the canonical path, multiple consecutive slashes are
        replaced by a single one.
{Fore.RESET}
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.path:
        result = Solution().simplifyPath(args.path[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
