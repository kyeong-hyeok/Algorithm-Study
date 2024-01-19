# 암호를 이루는 알파벳이 암호에서 증가하는 순서. abc (o) bac(x)
# 최소 한개 모음 최소 두개 자음 

import sys
from itertools import combinations

input=sys.stdin.readline

l,c=map(int,input().split())
arr=sorted(list(map(str,input().split())))
answer =[]

def backTracking(cnt,idx):
    if cnt == l:
        vo,co = 0,0
        
        for i in range(l):
            if answer[i] in ['a','e','i','o','u']:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print("".join(answer))
        return
    
    for i in range(idx,c):
        answer.append(arr[i])
        backTracking(cnt+1, i+1)
        answer.pop()

backTracking(0,0)
# for i in combinations(arr,l):
#     print(''.join(i))