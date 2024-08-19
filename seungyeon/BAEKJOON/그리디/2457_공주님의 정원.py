import sys

input=sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    m1,d1,m2,d2=map(int,input().split())
    arr.append([m1 * 100 + d1, m2 * 100 + d2])

arr.sort()
end_date = 301 # 최소 마지막 꽃이 지는 날짜 

answer = 0

while (arr):
    if (end_date >= 1201 or arr[0][0] > end_date): # 마지막 꽃 지는 날짜가 12/1 이상이거나, 확인할 꽃이 마지막 꽃과 이어지지 않을 때 (정렬을 헀기때문에)
        break

    tmp_end_date = -1

    for i in range(len(arr)):

        if (arr[0][0] <= end_date):

            if (tmp_end_date <= arr[0][1]):
                tmp_end_date = arr[0][1]

            arr.remove(arr[0])
        else:
            break

    end_date = tmp_end_date
    answer+=1

if end_date < 1201:
    print(0)
else:
    print(answer)

# visited 배열 365개를 모두 true / false 를 확인하기엔 시간이 많이 걸림
# day=[0,30,28,31,30,31,30,31,31,30,31,30,31]
# for i in range(len(day)-1):
#     day[i+1] += day[i]


# # 전체 날짜 
# visited=[False]*365


# n=int(input())
# arr=[]
# answer =0
# for i in range(n):
#     m1,d1,m2,d2=map(int,input().split())
#     open=day[m1-1]+d1
#     end=day[m2-1]+d2
#     arr.append([open,end])

# # 각 구간의 길이를 계산하는 함수 정의
# def interval_length(interval):
#     return interval[1] - interval[0]

# # arr을 각 구간의 길이에 따라 내림차순 정렬
# arr.sort(key=interval_length, reverse=True)


# for i in range(len(arr)):
#     if all(visited):
#         break
#     if i == len(arr) and not all (visited):
#         answer = 0
    
#     visited[arr[i][0]:arr[i][1]+1] = [True] * (arr[arr[i][1] - arr[i][0] + 1])
#     answer += 1

# print(answer)