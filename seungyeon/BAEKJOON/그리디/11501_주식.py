import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    answer = 0
    max = arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i] > max :
            max = arr[i]
        else:
            answer += max - arr[i]
    print(answer)

# def sum_arr(i,start):
#     sum = 0

#     for k in range(start,i):
#         sum += (arr[i]-arr[k])
#     return sum

# t=int(input())
# for _ in range(t):
#     n=int(input())
#     start ,answer,=0,0
#     arr=list(map(int,input().split()))
#     for i in range(1,n):
#         if arr[i-1] > arr[i]:
#             answer += sum_arr(i-1,start)
#             start = i
#         elif i == n-1:
#             answer += sum_arr(i,start)
#     print(answer)


