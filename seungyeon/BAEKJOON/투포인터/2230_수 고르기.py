import sys
input=sys.stdin.readline

n,m=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort()

l,r=0,0
answer=2000000000


while(r < n): # right를 움직이는 이유는 더 큰 숫자에서 현재 값을 빼서 더 큰 차이를 갖기 위해서

    if arr[r]-arr[l] > m:
        answer = min(answer,arr[r]-arr[l])
        l += 1
    elif arr[r]-arr[l] < m:
        r += 1
    else :
        answer = m
        break

print(answer)