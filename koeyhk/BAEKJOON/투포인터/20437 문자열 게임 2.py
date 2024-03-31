# T = 100
# 문자를 K개 포함하는 가장 짧은 연속 문자열의 길이
# 문자를 K개 포함하고, 첫번째와 마지막 글자가 해당 문자인 가장 긴 연속 문자열의 길이

# 각 문자가 등장하는 인덱스 순서대로 저장, 각 문자의 개수를 나타내는 cnt 저장

import sys

input_data = sys.stdin.readline

T = int(input_data())
for _ in range(T):      #O(TN)
    W = list(input_data().rstrip())
    K = int(input_data())
    inx = [[] for _ in range(26)]
    cnt = [0] * 26
    s, l = 100000, 0
    for i in range(len(W)):
        j = ord(W[i])-ord('a')
        cnt[j] += 1
        inx[j].append(i)
        if cnt[j] >= K:
            s = min(s, i - inx[j][len(inx[j])-K] + 1)
            l = max(l, i - inx[j][len(inx[j])-K] + 1)
    if s == 100000 or l == 0:
        print(-1)
    else:
        print(s, l)