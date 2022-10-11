#Read a given string, change the character at a given index and then print the modified string.

import string

def strReplace(s: string,a ,b : string):
    s = s[:int(a)] + b + s[(int(a) + 1):]
    print(s)

s = str(input('input string: '))
a = int(input('input position: '))
d = str(input('input character: '))
strReplace(s, a, d)
