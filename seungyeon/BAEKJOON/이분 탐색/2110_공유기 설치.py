# import sys
# input=sys.stdin.readline

# n,c=map(int,input().split())
# arr=[int(input()) for _ in range(n)]
# arr.sort()

# start = 1
# end = arr[-1] - arr[0] # 최대 공유기 거리
# answer = 0

# while start <= end :
#     cur = arr[0] # 현재 위치 
#     cnt = 1 # 공유기 설치 개수 
#     mid = (start+end) // 2 # 1-가장 먼 거리의 중간값. 이후 ?? 와 비교할 대상 

#     for i in range(1,n): # 입력받은 배열 작은 것부터 순회하면서
#         if arr[i] - cur >= mid: # 내가 설정한 가장 작은값과 순서대로 순회하는 변수의 차가 비교대상보다 크면 
#             cnt += 1 # 공유기 설치
#             cur = arr[i] # 현재 위치 cur 은 공유기 설치 노드로 변경 

#     if cnt >= c: # 공유기 설치 목표보다 큰데
#         if answer < mid: # 현재 위치가 크다면 
#             answer = mid # 답은 현재위치 
#         start = mid + 1 # 시작 기준을 중간 이후 값으로 
#     else :
#         end = mid -1 # 종료 기준을 중간 이전 값으로 

# print(answer)



import sys
input=sys.stdin.readline

n,c=map(int,input().split())
arr=[int(input()) for _ in range(n)]
arr.sort()

# 공유기 사이 거리를 이분 탐색으로 찾는다
# n 숫자를 공유기 사이 거리로 했을 때 c를 만족하면 ok, 만족하지 못하면 n (거리) 조절 

start = 1
end = arr[-1]-arr[0]
answer = 0 # 기본 0 

while (start <= end):

    cur = arr[0]
    cnt = 1

    mid = (start+end)//2

    for i in range(1,n):
        if arr[i] - cur >= mid:
            cnt += 1
            cur = arr[i]

    if cnt < c: # 목표 설치 개수보다 적으면 거리를 좁힌다
        end = mid - 1
    else:
        if answer < mid:
            answer = mid
        start = mid + 1

print(answer)