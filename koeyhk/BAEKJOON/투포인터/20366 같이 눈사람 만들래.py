# N개 눈덩이 지름 H (N = 600, H = 10^9)
# 눈사람 -> 두개 눈덩이 (위 <= 아래) 눈사람 키 = 두 눈덩이 지름 합
# 1 3 6 9 10
# 4 7 10 11, 9 12 13, 15 16, 19
# 키 차이 작은 눈사람
# 4개 고르기 -> 분배 - 시간 초과 O(N^4)
# 투포인터 -> 4개의 포인터로 이동하면서

# 문제 접근 -> 투포인터 o
# -> 4개의 포인터를 어떻게 이동해야 할지 감을 잡지 못 함

# 문제 풀이 아이디어
# 두 개의 포인터를 이중 for 문으로 구하고, 나머지 두 개의 포인터는 이분 탐색
# **이중 for 문으로 구할 때 i와 i+3 ~ N까지 수 중 하나 택하기**
# 이분 탐색으로 두 수 사이에 있는 두 개의 수를 구해야 하기 때문
# O(N^2) * (logN)

import sys

input_data = sys.stdin.readline

N = int(input_data())
H = list(map(int, input_data().split()))
H.sort()
result = 10e9
for i in range(N-3):
    for j in range(i+3, N):
        l, r = i + 1, j - 1
        while l <= r:
            tmp = (H[i] + H[j]) - (H[l] + H[r])
            result = min(result, abs(tmp))
            if tmp < 0:
                r -= 1
            else:
                l += 1

print(result)
