# 개선한 풀이
# dictionary에 각 알파벳이 가지는 수를 저장
# dictionary의 values로 리스트를 만들어 내림차순 정렬

import sys

input_data = sys.stdin.readline

N = int(input_data())
nums = [list(input_data().rstrip()) for _ in range(N)]
d = dict()
for num in nums:
    c = 1
    for i in range(len(num)-1, -1, -1):
        if num[i] in d:
            d[num[i]] += c
        else:
            d[num[i]] = c
        c *= 10

dl = list(d.values())
dl.sort(reverse=True)
result = 0
n = 9
for i in range(len(dl)):
    result += dl[i] * n
    n -= 1
print(result)


# 이전 풀이
# N = 10, 대문자, 대문자를 0~9 숫자 중 하나로 바꿔서 N개의 수 합하기
# 각 자릿수마다 알파벳 몇 개인지 확인 -> 가장 큰 자릿수에 많은 알파벳부터 배정
# 최대한 반례 보지 말고 혼자 생각해서 반례 찾기!!

# 생각하지 못한 부분
# 현재 자리의 개수가 10 이상이 될 경우 -> 다음 자리의 수 + 1, 현재 자리의 개수 - 10

import sys

input_data = sys.stdin.readline

N = int(input_data())
nums = [list(input_data().rstrip()) for _ in range(N)]
cnt = [[0]*8 for _ in range(26)]
for num in nums:
    c = 0
    for i in range(len(num)-1, -1, -1):
        cnt[ord(num[i])-ord('A')][c] += 1
        c += 1
for i in range(26):
    for j in range(7):
        if cnt[i][j] >= 10:
            cnt[i][j+1] += 1
            cnt[i][j] -= 10
cnt.sort(key=lambda x: (-x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))
result = 0
n = 9
for i in range(10):
    if max(cnt[i]) == 0:
        break
    c = 1
    for j in range(8):
        result += c * n * cnt[i][j]
        c *= 10
    n -= 1

print(result)