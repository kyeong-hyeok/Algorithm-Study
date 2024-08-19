import sys
input=sys.stdin.readline

n,m = map(int,input().split())
know = set(input().split()[1:])
party = []

for i in range(m):
    party.append(set(input().split()[1:]))

for i in range(m):
    for p in party:
        if p & know: # 파티 참석자 중 진실을 아는 사람이 있다면
            know = know.union(p) # 진실 아는 사람에 모두 더하기

cnt = 0
for p in party:
    if p & know: # 파티중에 진실을 아는 사람이 있다면 패스
        continue
    cnt += 1

print(cnt)