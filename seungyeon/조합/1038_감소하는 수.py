# 양수 x의 자릿수가 가장 큰 자릿수 부터 작은 자릿수까지 감소 -> 321 일 때 , 3 > 2 > 1, 950 일 떄 9 > 5 > 0
# N번째 감소하는 수 
# N의 최대 10000000 (100만)

# 같으면 안되고, 무조건 작아야함. 최대값 9876543210

# 9부터 0까지 2개 뽑기 -> 98,97,96, ... 90
# 9부터 0까지 n개 뽑기 -> n자리 수
from itertools import combinations

n = int(input())

result = []
for i in range(1, 11):
	for j in combinations(range(10), i): # i개 의 조합
		num = ''.join(list(map(str, reversed(list(j))))) # 조합한 숫자를 역순으로 -> 감소하는 수
		result.append(int(num))
result.sort()
if n >= len(result):
	print(-1)
else:
	print(result[n])