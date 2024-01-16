import sys
input = sys.stdin.readline

n,m=map(int,input().split())
num = [0]+ list(map(int,input().split()))
for i in range(len(num)-1):
    num[i+1] += num[i]
    
for i in range(m):
    x,y=map(int,input().split())
    print(num[y]-num[x-1])
