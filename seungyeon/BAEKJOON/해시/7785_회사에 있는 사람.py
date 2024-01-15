import sys
from collections import deque
input=sys.stdin.readline

arr={}
n = int(input())

for i in range(n):
    name,status=map(str,input().split())
    if status=='enter':
        arr[name]=True
    else:
        del arr[name]

print('\n'.join(sorted(arr,reverse=True)))