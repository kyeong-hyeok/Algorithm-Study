import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=dict()
for i in range(n):
    id,pw = input().split()
    arr[id] = pw

for j in range(m):
    find = input().rstrip()
    print(arr[find])