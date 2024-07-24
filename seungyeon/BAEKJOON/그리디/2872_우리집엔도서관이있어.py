import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

k = n
for i in range(n-1,-1,-1):
    if k == arr[i]:
        k -= 1

print(k)