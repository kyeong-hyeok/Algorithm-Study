import sys
input=sys.stdin.readline

n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort()

answer=[]
for j in arr:
    answer.append(j*n)
    n -= 1

print(max(answer))