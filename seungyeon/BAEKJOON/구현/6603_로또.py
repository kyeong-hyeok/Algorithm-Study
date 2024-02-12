import sys
from itertools import combinations

input=sys.stdin.readline

while True:
    arr=list(map(int,input().split()))

    if arr[0] == 0:
        break
    s = arr[1:]

    for i in combinations(s,6):
        print(*i)
    print()
