# 804. Unique Morse Code Words

import argparse
from colorama import Fore


class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        
        list_modifs = []
        
        for word in words:
            transferd_word = ''
            for el in word:
                n = ord(el)-97
                transferd_word += morse[n]
                
            if transferd_word not in list_modifs:
                list_modifs.append(transferd_word)
            

        return len(list_modifs)


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-w', '--words', type=str, nargs="+",
        help='Words array')
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
    # 804. Unique Morse Code Words


International Morse Code defines a standard encoding where each
letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.

Given an array of strings words where each word can be written as a
concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the
concatenation of "-.-.", ".-", and "-...". We will call such a
concatenation the transformation of a word.
Return the number of different transformations among all words
we have.
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = f'''
Example 1:
    $ python3 l-0804.py --words "gin" "zen" "gig" "msg"
    >>> 2
{Fore.GREEN}
    Explanation: The transformation of each word is:
    "gin" -> "--...-."
    "zen" -> "--...-."
    "gig" -> "--...--."
    "msg" -> "--...--."
    There are 2 different transformations: "--...-." and "--...--.".
{Fore.RESET}
Example 2:
    $ python3 l-0804.py --words "a"
    >>> 1
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.words:
        result = Solution().uniqueMorseRepresentations(args.words)
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=="__main__":
    main()