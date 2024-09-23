import sys
input=sys.stdin.readline

k,n=map(int,input().split())
arr=[]
for i in range(k):
    arr.append(int(input().rstrip()))

start,end=0,min(arr)
while(start<=end):

    mid = (start+end)//2
    sum = 0
    for i in arr:
        sum += i//mid

    if sum >= n:
        start = mid +1
    else:
        end = mid - 1

print(end)