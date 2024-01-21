# 뒤에서부터 깎으면 됨
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
answer = 0
for i in range(n):
    arr.append(int(input()))

for i in range(n-1,0,-1):
    if arr[i] <= arr[i-1]:
        answer += (arr[i-1] - arr[i]+1)
        arr[i-1] = arr[i]-1

print(answer)

