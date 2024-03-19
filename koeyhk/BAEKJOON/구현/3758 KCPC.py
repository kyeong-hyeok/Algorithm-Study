# k, n = 100 m = 10,000
# 점수 같다면 풀이 제출 횟수 적은 팀 -> 마지막 제출 시간 빠른 팀

import sys

input_data = sys.stdin.readline

T = int(input_data())
for _ in range(T):
    n, k, t, m = map(int, input_data().split())
    grade = [[0] * (k+1) for _ in range(n+1)]
    cnt = [0] * n       # 풀이 제출 횟수
    last = [0] * n      # 마지막 제출 시간
    for a in range(m):
        i, j, s = map(int, input_data().split())
        grade[i][j] = max(grade[i][j], s)
        cnt[i-1] += 1
        last[i-1] = a
    total = []          # 총점
    for i in range(1, n+1):
        total.append(sum(grade[i]))
    tot, c, l = total[t-1], cnt[t-1], last[t-1]
    rank = 1
    for i in range(n):
        if i != t-1:
            if total[i] > tot:
                rank += 1
            elif total[i] == tot and cnt[i] < c:
                rank += 1
            elif total[i] == tot and cnt[i] == c and last[i] < l:
                rank += 1
    print(rank)