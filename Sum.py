#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from array import array
from operator import index


def sumNum(lst, target):
    for i in range(len(lst)):
        for y in range(i+1, len(lst)):
            if (lst[i] + lst[y]) == target: 
                return [i, y]
    print('nothing')

lst = list(map(int, input("Each elements with space: ").strip().split()))
print(lst)
target = int(input('Target: '))
newList= sumNum(lst, target)
print(newList)