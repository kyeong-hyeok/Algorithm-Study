# N = 500,000, M = 500,000

# bisect 라이브러리 사용

import sys
from bisect import bisect_left, bisect_right

input_data = sys.stdin.readline

N = int(input_data())
num = list(map(int, input_data().split()))
M = int(input_data())
numm = list(map(int, input_data().split()))
num.sort()


def count(x):
    l = bisect_left(num, x)
    r = bisect_right(num, x)
    return r-l


for n in numm:
    print(count(n), end=' ')


# Counter 라이브러리 사용

import sys
from collections import Counter

input_data = sys.stdin.readline

N = int(input_data())
num = list(map(int, input_data().split()))
M = int(input_data())
numm = list(map(int, input_data().split()))
num.sort()

count = Counter(num)

for n in numm:
    if n in count:
        print(count.get(n), end=' ')
    else:
        print(0, end=' ')

# Dictionary

import sys

input_data = sys.stdin.readline

N = int(input_data())
num = list(map(int, input_data().split()))
M = int(input_data())
numm = list(map(int, input_data().split()))
num.sort()

count = dict()
for n in num:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

for n in numm:
    if n in count:
        print(count.get(n), end=' ')
    else:
        print(0, end=' ')

