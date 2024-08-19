import sys
n = int(input())
arr = list(map(int,input().split()))

answer =[0,0]

left,right,m = 0,n-1,sys.maxsize

while left < right:
    if abs(arr[left]+ arr[right]) < m:
        m = abs(arr[left]+arr[right])
        answer[0] = arr[left]
        answer[1] = arr[right]
    if arr[left] + arr[right] < 0:
        left += 1
    else:
        right -=1

print(answer[0],answer[1])