import random
import math
from numpy import *
import re
import string

# 1 point
print(sort(array(10*random.random(10), float)), end='\n\n')

# 2 point
c = zeros(8*8).reshape(8, 8)
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            c[i][j] = 1

print(c, end='\n\n')

# 3 point

print(dot(random.random((8, 4)), random.random((4, 2))), end='\n\n')

# 4 point

print(random.uniform(0, 1, 10))

# 5 point


def matrixs(numb):
    nums = []
    for multip in range(2, int(numb//2)):
        while numb % multip == 0:
            nums.append(multip)
            numb //= multip
    if numb != 1:
        nums.append(numb)
    print(nums, end='\n\n')
    if nums is False:
        print('Нельзя создать матрицу')
    else:
        for i in range(1, len(nums)):
            print(random.random((math.prod(nums[:i]), math.prod(nums[i:]))), random.random((math.prod(nums[i:]), math.prod(nums[:i]))), sep='\n\n', end='\n\n')


matrixs(24)

# 6 point


class search_text:

    def __init__(self, path_document):
        self.path_document = path_document

    def searching(self, word):
        a = open(self.path_document, 'r')
        dat = [i.split() for i in a.read().split('\n')]
        #print(dat)
        for i in range(len(dat)):
            for j in range(len(dat[i])):
                if re.findall(word, dat[i][j]):
                    print(f'{i+1} строка, {j+1} слово')


search_text('data.txt').searching('python')

# 7 point


def neural_network (vector, hight, last=False):
    B = 10*random.random((len(vector), hight))
    C = dot(vector, B)
    if last == False:

        D = sin(C)
        last = True
    else:
        D = maximum(C, 0)
        last = False
    return D, B

print('\n')
D, B = neural_network([1, 4, 7, 8, 9], 10)
print(D, B, sep='\n\n', end='\n\n')

D, B = neural_network([1, 4, 7, 8, 9], 5, True)
print(D, B, sep='\n\n', end='\n\n')