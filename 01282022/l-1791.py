# 1791. Find Center of Star Graph

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-ed', '--edges', type=str, nargs=1,
        help='Edges (input as string)')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def findCenter(self, edges: list) -> int:
        dct = {}
        
        for el1 in edges:
            for el in el1:
                if el not in dct:
                    dct[el] = 1
                else:
                    dct[el] += 1
        
        el = max(list(dct.values()))
        idx = list(dct.values()).index(el)
        
        lst = list(dct.keys())
        return lst[idx]


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1791. Find Center of Star Graph

There is an undirected star graph consisting of n nodes labeled from
1 to n. A star graph is a graph where there is one center node and
exactly n - 1 edges that connect the center node with every other
node.

You are given a 2D integer array edges where each edges[i] = [ui, vi]
indicates that there is an edge between the nodes ui and vi. Return
the center of the given star graph.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1791.py --edges "[[1,2],[2,3],[4,2]]"
    >>> 2
{Fore.GREEN}
    Explanation:
        As shown in the figure above, node 2 is connected to
        every other node, so 2 is the center.
{Fore.RESET}
Example 2:
    $ python3 l-1791.py --edges "[[1,2],[5,1],[1,3],[1,4]]"
    >>> 1
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.edges:
        edges = eval(args.edges[0])
        result = Solution().findCenter(edges)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()
