import sys
input=sys.stdin.readline

n = int(input())
card=list(map(int,input().split()))
bucket=dict()

for i in card:
    if bucket.get(i):
        bucket[i] = bucket.get(i)+ 1
    else:
        bucket[i] = 1

m = int(input())
num=list(map(int,input().split()))

answer = []
for i in num:
    if bucket.get(i):
        answer.append(bucket.get(i))
    else:
        answer.append(0)

print(*answer)