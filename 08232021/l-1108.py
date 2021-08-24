class Solution:
    def defangIPaddr(self, address: str) -> str:
        string = ''
        for el in address:
            if el == '.':
                string += ('[.]')
            else:
                string += el
                
        return string
