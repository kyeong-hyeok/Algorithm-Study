import sys
input=sys.stdin.readline

n,s = map(int,input().split())
arr=list(map(int,input().split()))

def back(x):
    global tmp,cnt
    if tmp == s:
        cnt += 1

    for i in range(x,n):
        tmp += arr[i]
        back(i+1)
        tmp -= arr[i]

tmp = 0
cnt = 0
back(0)


if s == 0:
    print(cnt -1)
else:
    print(cnt)

    
# arr.sort()

# l,r=0,n-1

# def find(l,r):
#     while( l< r):
#             if arr[l] + r  < 0:
#                 arr[l] += arr[r]
#                 r -= 1
#             elif arr[l] + r == 0:
#                 return True
#             elif arr[l] + r > 0:
#                 arr[l] += arr[r]
#                 l += 1

# answer = 0
# for i in range(n):
#     if find(i,n-1):
#          answer += 1
        
# print(answer)