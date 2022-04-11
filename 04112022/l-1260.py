# 1260. Shift 2D Grid

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-g', '--grid', type=str, nargs=1,
        help="Grid (input as integer)")
    parser.add_argument('-k', type=int, nargs=1,
        help='Integer K')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def shiftGrid(self, grid: list, k: int) -> list:
        elements = []
        
        for row in grid:
            elements += row
        
        if k > len(elements):
            k = k % len(elements)
        new_elements = elements[-k:] + elements[:-k]

        cols = len(grid[0])
        for idx, row in enumerate(grid):
            grid[idx] = new_elements[:cols]
            new_elements = new_elements[cols:]
        
        return grid


def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
Given a 2D grid of size m x n and an integer k. You need to shift the
grid k times.

In one shift operation:
    Element at grid[i][j] moves to grid[i][j + 1].
    Element at grid[i][n - 1] moves to grid[i + 1][0].
    Element at grid[m - 1][n - 1] moves to grid[0][0].
    Return the 2D grid after applying shift operation k times.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-1260.py --grid "[[1,2,3],[4,5,6],[7,8,9]]" -k 1
    >>> [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
    $ python3 l-1260.py --grid "[[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]" -k 4
    >>> [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
    $ python3 l-1260.py --grid "[[1,2,3],[4,5,6],[7,8,9]]" -k 9
    >>> [[1,2,3],[4,5,6],[7,8,9]]
    '''
    
    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.grid and args.k:
        grid = eval(args.grid[0])
        result = Solution().shiftGrid(grid, args.k[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
