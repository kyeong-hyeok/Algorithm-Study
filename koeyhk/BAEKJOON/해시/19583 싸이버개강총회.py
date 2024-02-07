# 누가 왔는지 알 수 없음, 끝까지 남아있는 사람 알 수 없음, 틀어놓기만 한지 알 수 없음
# 시작 전 입장 확인 여부 확인 -> 개강총회 시작까지 채팅기록
# 개총 끝, 스트리밍 끝까지 퇴장 여부 확인 -> 개총 끝나고 스트리밍 끝날 때까지 대화

# input 개수를 모를 때 입력 처리
# -> try except 구문

import sys

input_data = sys.stdin.readline

time = list(input_data().split())
seq = []
for t in time:
    a, b = t.split(":")
    seq.append(int(a)*60 + int(b))
enter = dict()
result = 0
while 1:
    try:
        ti, name = input_data().split()
        a, b = ti.split(":")
        t = int(a)*60 + int(b)
        if t <= seq[0]:
            enter[name] = 1
        elif seq[1] <= t <= seq[2] and name in enter:
            del enter[name]
            result += 1
    except:
        break

print(result)