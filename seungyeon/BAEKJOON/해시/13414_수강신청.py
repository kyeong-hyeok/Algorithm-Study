import sys
input=sys.stdin.readline
k,l=map(int,input().split())
arr=dict()

for i in range(l):
    str=input().rstrip()
    arr[str] = i

answer = sorted(arr.items(),key=lambda x: x[1])

if len(answer) < k:
    for i in range(len(answer)):
        print(answer[i][0])
else:
    for i in range(k):
        print(answer[i][0])
