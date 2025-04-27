# import sys

# m,n=map(int,input().split())

# for i in range(m,n+1):
#     if i == 1:
#         continue
#     is_prime=True
#     for j in range(2,int(i**0.5)+1): # i의의 제곱근을구해 나눠지는지 확인인
#         if i%j == 0:
#             # j 가 약수로 나뉘어 진다면 print 하지 않음
#             is_prime=False
#             break

#     if is_prime:
#         print(i)


import sys

n,m=int(input().split())

for i in range(n,m+1):
    for j in range(i,int(i**0.5)+1):
        if i % j == 0:
            break
    
    else:
        print(i)
