# 백트래킹 : 탐색하다가 더 갈 수 없으면 왔던 길을 되돌아가 다른 길을 찾는다
# 색칠 문제 
# 정점 i에 색상c를 칠하면 지금까지 칠해놓은 정점들과 색이 충돌하지 않는지 체크한다
# 이를 위해서는 정점 i에 인접하면서 이미 칠이 되어있는 정점 중 색상 c로 칠해진 정점이 있는지 확인하면 된다.

import sys
from collections import Counter

def backtraking(pre,l):
    answer = 0

    if l == len(lucky): # 행운의 문자열 answer += 1
        return 1
    
    for i in cnt.keys():
        if i == pre or cnt[i] == 0:
            continue

        cnt[i] -= 1
        answer += backtraking(i,l+1)
        cnt[i] += 1
    return answer 

lucky = list(map(str,sys.stdin.readline().strip()))
cnt = Counter(lucky)
print(backtraking('',0))