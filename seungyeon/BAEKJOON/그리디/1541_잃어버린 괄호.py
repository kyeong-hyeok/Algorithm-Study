# import sys
# from collections import deque

# input = sys.stdin.readline

# arr = input().strip() # 문자열 공백 제거
# new = arr.split('-') # 음수 기준 자르기

# answer = 0

# x=sum(map(int,(new[0].split('+')))) # 첫번쨰가 음수인 경우

# if arr[0] == '-':
#     answer -= x
# else:
#     answer += x

# for x in new[1:]: # 첫번쨰 이후
#     x = sum(map(int,(x.split('+'))))
#     answer -= x

# print(answer)










# # arr = re.split('([-|+])',arr)

# # num=deque()
# # opr=deque()

# # for i in range(len(arr)):
# #     if i%2:
# #         opr.append(arr[i])        
# #     else:
# #         num.append(int(arr[i])) 

# # num,opr 두 배열을 조합하면 된다고 생각했음. 아니었음


# -기준으로 나누고, 나눈 값 중 더하기가 있다면 더함. 이후에 뺌

import sys
input=sys.stdin.readline

sp=input().split('-')

num =[]

for i in sp:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)

    num.append(sum)

n = num[0]
for i in range(1,len(num)):
    n -= num[i]

print(n)