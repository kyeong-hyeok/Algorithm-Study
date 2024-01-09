import sys
from itertools import combinations

input = sys.stdin.readline # 속도 향상

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result =  sys.maxsize

house = []      
chick = []      

# 집과 치킨집 좌표 기록 (0(n^2))
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j]) 
        elif city[i][j] == 2:
            chick.append([i, j]) 

# m개 의 치킨집 조합으로 정해서 최소값 도시의 치킨 거리  구하기 
for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0                            
    for h in house: 
        chi_len = sys.maxsize  
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))  # 각 집의 치킨 거리
        temp += chi_len             # 도시의 치킨 거리
    result = min(result, temp)

print(result)