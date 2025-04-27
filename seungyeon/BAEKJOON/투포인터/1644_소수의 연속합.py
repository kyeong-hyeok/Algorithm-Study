import sys
input=sys.stdin.readline

n=int(input())

# 에라토스 테네스의 체

arr=[False,False] + [True] * (n-1)
prime=[]

for i in range(2,n+1):
    if arr[i]:
        prime.append(i)
        for j in range(2*i,n+1,i): # 소수의 배수는 모두 false 처리 
            arr[j] = False

answer = 0
start = 0
end = 0

while end <= len(prime):
    tmp = sum(prime[start:end])

    if tmp == n:
        answer += 1
        end += 1
    elif tmp < n:
        end += 1
    else :
        start += 1

print(answer)