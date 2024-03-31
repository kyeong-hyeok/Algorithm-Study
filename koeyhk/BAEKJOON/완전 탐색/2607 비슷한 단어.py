# 짧은 풀이 -> 52ms
# 완전 탐색 가능
# -> 한 단어를 기준으로 비교해서 존재한다면 기준 단어에서 해당 문자 remove
# -> 한 단어를 기준으로 비교해서 존재하지 않는다면 cnt += 1
# cnt가 2보다 작고, 기준으로 한 단어의 개수가 2보다 작을 경우 result += 1

import sys

input_data = sys.stdin.readline

N = int(input_data())
target = list(input_data().rstrip())

result = 0
for _ in range(N-1):
    t = target[:]
    str = list(input_data().rstrip())
    cnt = 0
    for s in str:
        if s in t:
            t.remove(s)
        else:
            cnt += 1
    if cnt < 2 and len(t) < 2:
        result += 1

print(result)


# 이전 풀이 -> 40ms
# 같은 종류의 문자, 같은 문자는 같은 개수만큼 -> 같은 구성
# 한 단어에서 한 문자를 더하거나, 빼거나, 하나를 다른 문자로 바꿨을 때 같음 -> 비슷한 단어
# 단어 전체의 개수 구해서 개수 숫자 차이 1인 거 2개까지 가능

# 처음에 놓친 부분
# 단어 a, b에서 a가 2개 많거나 b가 2개 많으면 안 됨
# 단어 a, b 각각 하나가 많거나, a만 하나 많거나, b만 하나 많거나

import sys

input_data = sys.stdin.readline

N = int(input_data())
cnt = [[0] * 26 for _ in range(N)]
s = list(input_data().rstrip())
for j in range(len(s)):
    cnt[0][ord(s[j])-ord('A')] += 1

result = 0
for i in range(1, N):
    s = list(input_data().rstrip())
    for j in range(len(s)):
        cnt[i][ord(s[j])-ord('A')] += 1
    a, b, p = 0, 0, 1
    for j in range(26):
        k = cnt[0][j] - cnt[i][j]
        if abs(k) >= 2:
            a = 3
        elif k == 1:
            a += 1
        elif k == -1:
            b += 1
        if a >= 2 or b >= 2:
            p = 0
            break
    if p:
        result += 1

print(result)