# 289. Game of Life

import argparse
from colorama import Fore

def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    
    parser.add_argument('-b', '--board', type=str, nargs=1,
        help='Board (input as string)')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def gameOfLife(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cells_to_change = []      
        
        for y, row in enumerate(board):
            for x, el in enumerate(row):
                counter = 0
                
                # Check row above
                if y > 0:
                    # Check left above
                    if x > 0:
                        if board[y-1][x-1]:
                            counter += 1
                    # Check just above
                    if board[y-1][x]:
                        counter += 1
                    # Check right above
                    if x < len(board[0]) - 1:
                        if board[y-1][x+1]:
                            counter += 1
                
                # Check current row
                # Check Left
                if x > 0:
                    if board[y][x-1]:
                        counter += 1
                    
                # Check right 
                if x < len(board[0]) - 1:
                    if board[y][x+1]:
                        counter += 1
                
                # Check row below
                if y < len(board) - 1:
                    # Check left below
                    if x > 0:
                        if board[y+1][x-1]:
                            counter += 1
                    # Check just below
                    if board[y+1][x]:
                        counter += 1
                    # Check right below
                    if x < len(board[0]) - 1:
                        if board[y+1][x+1]:
                            counter += 1
                
                # Check counter
                # IF CELL ALIVE
                if board[y][x]:
                    if counter < 2 or counter > 3:
                        cells_to_change.append([y,x])
                
                # IF CELL DEAD
                else:
                    if counter == 3:
                        cells_to_change.append([y,x])
        # Change cells
        for y, x in cells_to_change:
            if board[y][x]:
                board[y][x] = 0
            else:
                board[y][x] = 1
        return board

def main():
    descr = f'''
{Fore.RED+("="*70)+Fore.RESET}
{Fore.GREEN}
    # 289. Game of Life

According to Wikipedia's article: "The Game of Life, also known
simply as Life, is a cellular automaton devised by the British
mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has
an initial state: live (represented by a 1) or dead (represented by
a 0). Each cell interacts with its eight neighbors (horizontal,
vertical, diagonal) using the following four rules (taken from the
above Wikipedia article):

    1. Any live cell with fewer than two live neighbors dies as if
    caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the
    next generation.
    3. Any live cell with more than three live neighbors dies, as if
    by over-population.
    4. Any dead cell with exactly three live neighbors becomes a live
    cell, as if by reproduction.

The next state is created by applying the above rules simultaneously
to every cell in the current state, where births and deaths occur
simultaneously. Given the current state of the m x n grid board,
return the next state.
{Fore.RESET}
{Fore.RED+("="*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0289.py --board "[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]"
    >>> [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
    $ python3 l-0289.py --board "[[1,1],[1,0]]"
    >>> [[1,1],[1,1]]
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.board:
        board = eval(args.board[0])
        result = Solution().gameOfLife(board)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
