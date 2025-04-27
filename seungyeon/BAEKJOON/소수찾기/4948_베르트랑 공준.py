# import sys


# def get_decimal(n):

#     cnt = 0
#     if n == 1: return 1

#     for i in range(n+1,2*n+1):
#         for j in range(2,int(i**0.5)+1):
#             if i%j == 0:
#                 break
#         else:
#             cnt += 1

#     return cnt


# while (True):
#     n = int(input().rstrip())

#     if n == 0:
#         break

#     # 소수 개수 찾기
#     print(get_decimal(n))


num = 123456*2 + 1
arr=[1]*num

for i in range(1,num):
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            arr[i] = 0
            break


while True:
    x = int(input())

    if x == 0:
        break

    sum = 0
    for i in range(x+1,2*x+1):
        sum += arr[i]

    print(sum)

