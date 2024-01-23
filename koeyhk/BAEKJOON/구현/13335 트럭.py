# 문제 풀 때 생각한 것
# 1. 다리를 한꺼번에 건널 수 있는 트럭 결정
# 2. 다리를 건넌 트럭 하중 빼기

# 문제 풀 때 생각해야 할 것!
# 잘못된 부분 1~2개로 예제가 틀리는 경우
# -> 예제에서 어느 부분에 오류가 있는지 출력 확인하는 것이 중요

# 잘못 생각한 부분
# 트럭이 빠지고 새 트럭이 들어가는 것을 if else로 나눔
# -> 트럭이 빠지고 들어가는 것이 동시에 일어날 수 있으므로 나누면 안 됨

import sys

input_data = sys.stdin.readline
n, w, L = map(int, input_data().split())
truck = list(map(int, input_data().split()))
i, t = 1, 1
total = truck[0]
bridge_truck = [[truck[0], w]]      # [트럭 무게, 다리 끝에 도달하는 시간] -> 기준이 중요!
while i < n:
    if len(bridge_truck) > 0 and bridge_truck[0][1] == t:
        total -= bridge_truck[0][0]
        del bridge_truck[0]
    if truck[i] <= L - total:
        total += truck[i]
        bridge_truck.append((truck[i], t + w))
        i += 1
    t += 1

print(bridge_truck[len(bridge_truck)-1][1]+1)