# 824. Goat Latin

import argparse
from colorama import Fore


def BuildArgParser(descr):
    parser = argparse.ArgumentParser(descr)
    parser.add_argument('-s', '--sentence', type=str, nargs=1,
        help='Sentence')
    
    parser.add_argument('-d', '--description', action='store_true',
        help='Show description')
    parser.add_argument('-e', '--example', action='store_true',
        help='Show example')
    
    return parser


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        for id, word in enumerate(sentence.split(' ')):
            
            new_word = ''
            
            if word[0].lower() in 'aeiou':
                new_word = word + 'ma'
            
            else:
                new_word = word[1:] + word[0] + 'ma'
            
            new_word += 'a' * (id + 1)
            res.append(new_word)
        
        return ' '.join(res)


def main():
    descr = f'''
{Fore.RED+('='*70)+Fore.RESET}
{Fore.GREEN}
    # 824. Goat Latin

You are given a string sentence that consist of words separated by
spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up
language similar to Pig Latin.) The rules of Goat Latin are as
follows:

    1. If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'),
        append "ma" to the end of the word.
        For example, the word "apple" becomes "applema".

    2. If a word begins with a consonant (i.e., not a vowel), remove
        the first letter and append it to the end, then add "ma".
        For example, the word "goat" becomes "oatgma".

    3. Add one letter 'a' to the end of each word per its word index
        in the sentence, starting with 1.
        For example, the first word gets "a" added to the end, the
        secondword gets "aa" added to the end, and so on.

Return the final sentence representing the conversion from sentence to Goat Latin.
{Fore.RESET}
{Fore.RED+('='*70)+Fore.RESET}
    '''

    example = '''
Example 1:
    $ python3 l-0824.py --sentence "I speak Goat Latin"
    >>> "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:
    $ python3 l-0824.py --sentence "The quick brown fox jumped over the lazy dog"
    >>> "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    '''

    parser = BuildArgParser(descr)
    args = parser.parse_args()

    if args.sentence:
        result = Solution().toGoatLatin(args.sentence[0])
        print(result)
    
    elif args.description:
        print(descr)
    
    elif args.example:
        print(example)
    
    else:
        parser.print_help()


if __name__=='__main__':
    main()
    