# # # 암호를 이루는 알파벳이 암호에서 증가하는 순서. abc (o) bac(x)
# # # 최소 한개 모음 최소 두개 자음 

# # import sys
# # from itertools import combinations

# # input=sys.stdin.readline

# # l,c=map(int,input().split())
# # arr=sorted(list(map(str,input().split())))
# # answer =[]

# # def backTracking(cnt,idx):
# #     if cnt == l:
# #         vo,co = 0,0
        
# #         for i in range(l):
# #             if answer[i] in ['a','e','i','o','u']:
# #                 vo += 1
# #             else:
# #                 co += 1

# #         if vo >= 1 and co >= 2:
# #             print("".join(answer))
# #         return
    
# #     for i in range(idx,c):
# #         answer.append(arr[i])
# #         backTracking(cnt+1, i+1)
# #         answer.pop()

# # backTracking(0,0)
# # # for i in combinations(arr,l):
# # #     print(''.join(i))

# import sys
# input=sys.stdin.readline

# l,c=map(int,input().split())
# arr=sorted(list(map(str,input().split())))
# answer=[]

# # 정렬되어있는 모음1자음2

# def back(cnt,index):
#     if cnt == l: # 길이가 L이 되면 자음,모음 체크. 맞으면 print
#         vo,co=0,0

#         for i in range(l):
#             if answer[i] in  ['a','e','i','o','u']:
#                 vo += 1
#             else: 
#                 co += 1

#         if vo >= 1 and co >=2 :
#             print("".join(answer))
#         return
    
#     for i in range(index,c):
#         answer.append(arr[i])
#         back(cnt+1,i+1)
#         answer.pop()

# back(0,0)





import sys

input=sys.stdin.readline

l,c=map(int,input().split(" "))
inputs=list(map(str,input().rstrip().split()))

arr = ["a","e","i","o","u"]

# 최소 1개 모음, 두개 자음

inputs.sort()
answer=[]

visited=[False]*c

def check(password):
    cnt,other = 0,0
    
    for i in password:
        if i in arr:
            cnt += 1
        else:
            other += 1

    # if cnt >= 2 or other >= 3:
    #     False
    # else:
    #     True

    return  cnt >= 1 and other >= 2

def dfs(index):


    if len(answer) == l:
        if check(answer):
            print(''.join(answer))
        return 

    for i in range(index,c):
            if not visited[i]:
                answer.append(inputs[i])
                dfs(i+1)
                answer.pop()
                visited[i] = False

dfs(0)

            