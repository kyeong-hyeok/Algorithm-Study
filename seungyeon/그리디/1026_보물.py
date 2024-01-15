import sys
input=sys.stdin.readline

n = int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
sum = 0

for i in range(n):
    sum += max(b)*a[i]
    b.remove(max(b))
print(sum)