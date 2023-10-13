# 인접한 수가 같아도 오름차순 -> 중복 조합
# 길이가 N인 오르막수 -> n개 뽑기 
# 최악의 경우 N*N = 1000*1000 = 1000000 -> 

from itertools import combinations_with_replacement


arr = [1,2,3,4,5,6,7,8,9,0]

n = int(input())

print(len(list(combinations_with_replacement(arr,n)))%10007)

