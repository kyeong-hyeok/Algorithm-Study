# 앞선 수의 각 자리수의 제곱의 합
import sys
input=sys.stdin.readline
a,p=map(int,input().split())
arr=[a]

while True:

    tmp = 0
    for i in str(arr[-1]):
        tmp += int(i) ** p

    if tmp in arr: # 반복 시작
        break

    arr.append(tmp)

print(arr.index(tmp))