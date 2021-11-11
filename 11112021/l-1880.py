# 1880. Check if Word Equals Summation of Two Words

import argparse
import string
from colorama import Fore


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('-fw', '--firstword', type=str, nargs=1, help='First Word')
	parser.add_argument('-sw', '--secondword', type=str, nargs=1, help='Second Word')
	parser.add_argument('-tw', '--targetword', type=str, nargs=1, help='Target Word')
	parser.add_argument('-d', '--description', action='store_true', help='Show description')
	parser.add_argument('-e', '--example', action='store_true', help='Show example')

	return parser 


import string


# Get index numbers of word
def get_number(word, letters):
    num = ''
    for letter in word:
        ind = letters.index(letter)
        num += str(ind)
    num = int(num)
    return num
    
    
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # Get list of letters
        letters = list(string.ascii_lowercase)
        
        # Generate numbers indexes from words
        first_num = get_number(firstWord, letters)
        second_num = get_number(secondWord, letters)
        target_num = get_number(targetWord, letters)
        
        # Check if summation of numerical values of words rquals the numerical value of target
        return first_num + second_num == target_num


def main():
	descr = f'''
{Fore.RED}======================================================================{Fore.RESET}
{Fore.GREEN}
	# 1880. Check if Word Equals Summation 
	           of Two Words

The letter value of a letter is its position in the 
alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English 
letters s is the concatenation of the letter values of 
each letter in s, which is then converted into an integer.

For example, if s = "acb", we concatenate each letter's 
letter value, resulting in "021". After converting it, 
we get 21.
You are given three strings firstWord, secondWord, and 
targetWord, each consisting of lowercase English 
letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of 
firstWord and secondWord equals the numerical value of targetWord, 
or false otherwise.
{Fore.RESET}
{Fore.RED}======================================================================{Fore.RESET} 
	'''

	example = f'''
Example 1:
	$ python3 l-1880.py --firstword "acb" --secondword "cba" --targetword "cdb"
	>>> True
{Fore.GREEN}
	Explanation:
	The numerical value of firstWord is "acb" -> "021" -> 21.
	The numerical value of secondWord is "cba" -> "210" -> 210.
	The numerical value of targetWord is "cdb" -> "231" -> 231.
	We return true because 21 + 210 == 231.
{Fore.RESET}
Example 2:
	$ python3 l-1880.py --firstword "aaa" --secondword "a" --targetword "aab"
	>>> False
{Fore.GREEN}
	Explanation: 
	The numerical value of firstWord is "aaa" -> "000" -> 0.
	The numerical value of secondWord is "a" -> "0" -> 0.
	The numerical value of targetWord is "aab" -> "001" -> 1.
	We return false because 0 + 0 != 1.
{Fore.RESET}
Example 3:
	$ python3 l-1880.py --firstword "aaa" --secondword "a" --targetword "aaaa"
	>>> True
{Fore.GREEN}
	Explanation: 
	The numerical value of firstWord is "aaa" -> "000" -> 0.
	The numerical value of secondWord is "a" -> "0" -> 0.
	The numerical value of targetWord is "aaaa" -> "0000" -> 0.
	We return true because 0 + 0 == 0.
{Fore.RESET}
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.firstword and args.secondword and args.targetword:
		result = Solution().isSumEqual(args.firstword[0], args.secondword[0], args.targetword[0])
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	main()
        
