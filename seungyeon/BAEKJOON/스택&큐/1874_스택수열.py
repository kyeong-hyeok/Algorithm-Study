# # push 는 오름차순
#  # 임의의 수열이 있을 때 스택으로 그 수열을 만들 수 있는지
# # 있다면 어떤순서로 push ,pop 을 해야하는지 

# import sys
# input=sys.stdin.readline

# n=int(input().rstrip())
# arr=[]
# for i in range(n):
#     arr.append(int(input().rstrip()))

# stack=[]
# index = 0

# for i in range(1,n+1):

#     if i > index:
#         print('NO')
#         break

#     if stack and stack[-1] == arr[index]:
#         stack.pop()
#         print('-')
#         index += 1
#     else:
#         stack.append(i)
#         print('+')

#     if i == n and stack:
#         for i in range(len(stack)):
#             print('-')
#     elif i == n and not stack :
#         print('NO') 
    



import sys
input=sys.stdin.readline

n=int(input().rstrip())

stack=[]
index = 0

now = 1
ans = []
find = True
for _ in range(n):

    num = int(input())

    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        find = False

if not find:
    print('NO')
else:
    for i in ans:
        print(i)


