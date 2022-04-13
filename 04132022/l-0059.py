# 59. Spiral Matrix II

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-n', type=int, nargs=1,
        help='Integer N')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show description')
    
    return parser


class Solution:
    def generateMatrix(self, n: int) -> list:
        if n == 1:
            return [[1]]
        
        # create empty n x n matrix
        mat = []
        for _ in range(n):
            tmp = [0] * n
            mat.append(tmp)
        
        i = 1
        y, x = 0, 0
        while i < n*n:
            # Going right
            while True:
                if x + 1 < n and not mat[y][x+1]:
                    mat[y][x] = i
                    x += 1
                    i += 1
                else:
                    mat[y][x] = i
                    break
            
            # Going down
            while True:
                if y + 1 < n and not mat[y+1][x]:
                    mat[y][x] = i
                    y += 1
                    i += 1
                else:
                    mat[y][x] = i
                    break
            
            # Going left
            while True:
                if x > 0 and not mat[y][x-1]:
                    mat[y][x] = i
                    x -= 1
                    i += 1
                else:
                    mat[y][x] = i
                    break
            
            # Going up
            while True:
                if y > 0 and not mat[y-1][x]:
                    mat[y][x] = i
                    y -= 1
                    i += 1
                else:
                    mat[y][x] = i
                    break

        return mat


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with
elements from 1 to n2 in spiral order.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0059.py -n 3
    >>> [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
    $ python3 l-0059.py -n 1
    >>> [[1]]
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.n:
        result = Solution().generateMatrix(args.n[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
