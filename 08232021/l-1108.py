import sys

class Solution:
    def defangIPaddr(self, address: str) -> str:
        string = ''
        for el in address:
            if el == '.':
                string += ('[.]')
            else:
                string += el
                
        return string

def Main():
    argumentlist = sys.argv[1:]
    first = argumentlist[0]

    if first == '-d':
        print("Given a valid (IPv4) address, returned defanged version of of that IP address")

    elif first == '--help' or first == '-h':
        print('[-d] - description\n[-e] - one example how to use it\n[-args] - arguments throught comma')

    elif first == '-e':
        print('Input: 0.0.0.1\nOutput: 0[.]0[.]0[.]1')

    if first == '-args':
        for el in argumentlist[1:]:
            result = (Solution().defangIPaddr(el))
            print(f'Input: {el}')
            print(f'Output: {result}')

if __name__ == "__main__":
    Main()

# Input: "0.0.0.1"
# Output: "0[.]0[.]0[.]1"

# Input "0.0"
# Output: "0[.]0"
