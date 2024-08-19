import sys
input = sys.stdin.readline

N,d,k,c=map(int,input().split())
arr=[]
count = 0
for i in range(N):
    arr.append(int(input()))
    
for i in range(N):
    # arr[i] ~ arr[i+k] + c

    # i+k > N
    if i+k>N:
        sub = set(arr[i:N]+arr[:(i+k)%N] + [c])
    else:
        sub = set(arr[i:i+k] + [c])

    if count < len(sub):
        count = len(sub)
    
print(count)