# 선택 정렬
# 슬라이싱을 이용
# 버블 정렬을 이용해도 문제 해결 가능

import sys

input_data = sys.stdin.readline

P = int(input_data())
for i in range(1, P+1):
    th = list(map(int, input_data().split()))
    t = th[0]
    h = th[1:]
    cnt = 0
    for j in range(1, 20):
        for k in range(j):
            if h[j] < h[k]:
                h = h[:k] + [h[j]] + h[k:j] + h[j+1:]
                cnt += j-k
                break
    print(i, cnt)