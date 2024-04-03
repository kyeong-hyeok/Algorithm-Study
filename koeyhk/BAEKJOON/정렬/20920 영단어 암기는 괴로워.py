# 자주 나오면 앞에 -> 길수록 앞에 -> 사전 순으로 앞에
# N = 100,000 M = 10
# 길이가 M 이상인 단어들만!

import sys
from collections import Counter

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
words = [input_data().rstrip() for _ in range(N)]
words_cnt = Counter(words)
words = []
for k, v in words_cnt.items():
    l = len(k)
    if l < M:
        continue
    words.append([k, v, l])
words.sort(key=lambda x: (-x[1], -x[2], x[0]))

for word in words:
    print(word[0])