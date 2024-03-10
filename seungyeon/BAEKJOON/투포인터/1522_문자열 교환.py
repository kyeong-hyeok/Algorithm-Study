import sys
input = sys.stdin.readline

arr=list(input())
a_cnt=arr.count('a') # a 개수. a를 모두 연속하는 슬라이딩 윈도우의 크기
answer = 999999999999999
left = 0

while left < len(arr):
    right = left + a_cnt

    if right > len(arr): # 원형 문자열
        tmp = arr[left:len(arr)] + arr[:right-len(arr)]
    else:
        tmp = arr[left:right]
    answer = min(answer,tmp.count('b'))
    left += 1

print(answer)