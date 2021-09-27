# 929. Unique Email Addresses 


from colorama import Fore
import argparse


def BuildArgParser(descr):
	parser = argparse.ArgumentParser(descr)
	parser.add_argument('--emails', type=str, metavar='email',
		nargs='+', help='Array with emails')
	parser.add_argument('-d', '--description', action='store_true',
		help='Show description')
	parser.add_argument('-e', '--example', action='store_true',
		help='Show example')

	return parser 


class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        dct = {}
        
        for email in emails:
            # get domain
            for index, el in enumerate(email):
                if el == '@':
                    domain = email[index+1:]
                    local_name = email[:index]
                    break
            
            # get clean local name
            clean_local_name = ''
            for el in local_name:
                if el == '+':
                    break
                if el != '.':
                    clean_local_name += el
            
            # write dictionary
            new_email = f'{clean_local_name}@{domain}'
            if new_email not in dct:
                dct[new_email] = 1
            else:
                dct[new_email] += 1
        
        # return number of different addresses
        return len(dct)


def Main():
	descr = f'''
{Fore.RED}============================================================================={Fore.RESET}
	{Fore.GREEN}
	# 929. Unique Email Addresses 

Every valid email consists of a local name and a 
domain name, separated by the '@' sign. Besides 
lowercase letters, the email may contain one or 
more '.' or '+'.

Given an array of strings emails where we send one email to each 
email[i], return the number of different addresses that actually 
receive mails.
{Fore.RESET}
{Fore.RED}============================================================================={Fore.RESET}
	'''

	example = f'''
Example 1:
	$ python3 l-0929.py --emails "test.email+alex@leetcode.com" "test.e.mail+bob.cathy@leetcode.com"
	"testemail+david@lee.tcode.com"

	>>> 2

	{Fore.GREEN}Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.{Fore.RESET}

Example 2:
	$ python3 l-0929.py --emails "a@leetcode.com" "b@leetcode.com" "c@leetcode.com"
	>>> 3
	'''

	parser = BuildArgParser(descr)
	args = parser.parse_args()

	if args.emails:
		result = Solution().numUniqueEmails(args.emails)
		print(result)

	elif args.description:
		print(descr)

	elif args.example:
		print(example)

	else:
		parser.print_help()


if __name__=='__main__':
	Main()
