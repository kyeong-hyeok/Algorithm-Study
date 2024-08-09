# 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합

import sys
input=sys.stdin.readline

n=input()

arr=list(map(int,input().split(" ")))
for i in range(1,len(arr)):
    arr[i] = max(arr[i],arr[i]+arr[i-1]) # 연속한 수의 최대값이니까, 이전 값과 비교해서 현재 값이 제일 크면 됨 

print(max(arr))