import sys

input=sys.stdin.readline
n,m=map(int,input().split())
arr=[int(input()) for i in range(n)]

# input의 최대길이가 지나치게 길고, 특정 값을 찾아야 하는 문제라면 이분탐색을 의심하기
# 찾아야하는 값을 mid 로 놓고 조절해서 찾기

start,end=min(arr),max(arr) * m

answer = end

while start <= end:
    cnt = 0
    mid =  (start+end)//2

    for i in range(n):
        cnt += mid // arr[i]

    if cnt >= m: # 심사받은 친구의 합이 크다면 , 범위 줄이기 
        end = mid - 1
        answer = min(mid,answer)

    else: # 합이 작다면 범위 키우기
        start = mid + 1

print(answer)