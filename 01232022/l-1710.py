# 1710. Maximum Units on a Truck

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-bt', '--boxTypes', type=str , nargs=1,
        help='Box Types (input as string)')
    parser.add_argument('-ts', '--truckSize', type=int, nargs=1,
        help='Truck Size')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def maximumUnits(self, boxTypes: list, truckSize: int) -> int:
        dct = {}
        
        for idx, el in enumerate(boxTypes):
            dct[idx] = el[1]
        
        result = []
        for el in dct:
            
            n = max(list(dct.values()))
            idx = list(dct.values()).index(n)
            
            dct[idx] = -1
            
            box = boxTypes[idx]
            num = box[0]
            units = box[1]
            
            
            if truckSize >= num:
                truckSize -= num
                result.append(num * units)
            else:
                num = truckSize
                truckSize = 0
                result.append(num * units)
            
        
        return sum(result)


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 1710. Maximum Units on a Truck

You are assigned to put some amount of boxes onto one truck. You are
given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi,
numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number
of boxes that can be put on the truck. You can choose any boxes to
put on the truck as long as the number of boxes does not exceed
truckSize.

Return the maximum total number of units that can be put on the truck.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-1710.py --boxTypes "[[1,3],[2,2],[3,1]]" --truckSize 4
    >>> 8
{Fore.GREEN}
    Explanation: There are:
        - 1 box of the first type that contains 3 units.
        - 2 boxes of the second type that contain 2 units each.
        - 3 boxes of the third type that contain 1 unit each.
    You can take all the boxes of the first and second types, and one
    box of the third type.
    The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
{Fore.RESET}
Example 2:
    $ python3 l-1710.py --boxTypes "[[5,10],[2,5],[4,7],[3,9]]" --truckSize 10
    >>> 91 
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.boxTypes and args.truckSize:
        boxTypes = eval(args.boxTypes[0])
        result = Solution().maximumUnits(boxTypes, args.truckSize[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()

