# 그리디 -> x 오름차순 정렬, end 갱신

# 개선한 부분
# end를 갱신 시 heapq를 이용하여 제일 큰 끝점을 선택하는 방식 사용
# -> 끝나는 점의 최댓값만 필요하기 때문에 갱신만 시켜주면 된다! heapq를 사용하지 않고 end 갱신

import sys

input_data = sys.stdin.readline

N = int(input_data())
line = [list(map(int, input_data().split())) for _ in range(N)]
line.sort()     # O(NlogN)
start = line[0][0]
end = line[0][1]
result = 0
i = 1
while i < N:        # O(N)
    if line[i][0] > end:        # 겹치지 않을 때
        result += line[i][0] - end      # 마지막에 빼야하는 값(중간에 빈 부분) 저장
    end = max(end, line[i][1])
    i += 1
print(end - start - result)

