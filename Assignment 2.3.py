#You are given words. Some words may repeat. For each word, output its number of occurrences.
#The output order should correspond with the input order of appearance of the word.

import collections

lst = []
numStr = int(input('so chuoi nhap vao '))
for i in range(0, numStr):
    ele = input()
    lst.append(ele)
print(len(set(lst))) # dung set() vi moi phan tu cua no la rieng biet va khong lap lai
c = collections.Counter(lst)
for i in c:
    print(c[i], end=" ") # in ra so lan lap lai cua moi ele
print()
