# 1103. Distribute Candies to People

import argparse
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-c', '--candies', type=int, nargs=1, help='Number of candies')
	parser.add_argument('-p', '--people', type=int, nargs=1, help='Number of people')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')
	
	return parser 


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list:
        counter = 1
        
        result = [0 for i in range(num_people)]
        
        while candies > 0:
            for index, el in enumerate(result):
                if candies > 0:
                    if candies > counter:
                        candies -= counter
                        result[index] += counter
                        counter += 1
                    else:
                        result[index] += candies
                        candies -= counter
                        counter += 1
            
        return result


def main():
	descr = f''''
{Fore.RED}======================================================================{Fore.RESET}
{Fore.GREEN}
	# 1103. Distribute Candies to People

We distribute some number of candies, to a row of n = num_people 
people in the following way:

We then give 1 candy to the first person, 2 candies to the second 
person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to 
the first person, n + 2 candies to the second person, and so on 
until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, 
and moving to the start of the row after we reach the end) until 
we run out of candies.  The last person will receive all of our 
remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that 
represents the final distribution of candies.
{Fore.RESET}
{Fore.RED}======================================================================{Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-1103.py --candies 7 --people 4
	>>> [1,2,3,1]
{Fore.GREEN}
	Explanation:
		On the first turn, ans[0] += 1, and the array is [1,0,0,0].
		On the second turn, ans[1] += 2, and the array is [1,2,0,0].
		On the third turn, ans[2] += 3, and the array is [1,2,3,0].
		On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
{Fore.RESET}
Example 2:
	$ python3 l-1103.py --candies 10 --people 3
	>>> [5,2,3]
{Fore.GREEN}
	Explanation: 
	On the first turn, ans[0] += 1, and the array is [1,0,0].
	On the second turn, ans[1] += 2, and the array is [1,2,0].
	On the third turn, ans[2] += 3, and the array is [1,2,3].
	On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.candies and args.people:
		result = Solution().distributeCandies(args.candies[0], args.people[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=="__main__":
	main()