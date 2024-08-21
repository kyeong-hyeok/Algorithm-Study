import sys
input=sys.stdin.readline

n = int(input())
arr=[]
for i in range(n):
    start,end=map(int,input().split())

    arr.append((start,end))


# 빨리 끝나는 회의 순서대로 정렬을 해야 한다. 이유는 간단하다. 빨리 끝날수록 뒤에서 고려해볼 회의가 많기 때문이다. 
# 빨리 시작하는 순서대로 정렬을 우선 한다면, 오히려 늦게 끝날 수 있기 때문이다.

arr.sort(key=lambda x: (x[1],x[0]))

e = arr[0][1]

cnt = 1
for i in range(1,n):    
    if arr[i][0] >= e:
        cnt += 1
        e = arr[i][1]
    

print(cnt)