# 집합안에 포함되는 세수의 합인데 가장 큰거 

import sys
input=sys.stdin.readline

n,m=map(int,(input().split()))

arr=list(map(int,input().split()))

l,r=0,1

cnt =0
while(True):

    if r > n or l >r : 
        break

    sum_arr=arr[l:r]
    total=sum(sum_arr)

    if total == m:
        cnt += 1
        r += 1
    elif total < m:
        r += 1
    else:
        l += 1

 

print(cnt)

