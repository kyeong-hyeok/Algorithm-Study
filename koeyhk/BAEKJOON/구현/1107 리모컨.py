# 시간 초과 풀이
import sys

input_data = sys.stdin.readline

N = int(input_data())
M = int(input_data())
l = len(str(N))

if M == 0:  # 고장난 버튼이 없을 경우 출력 후 종료
    print(min(abs(N-100), l))
    exit()

broken = set(map(int, input_data().split()))
button = set()  # 작동하는 버튼
for i in range(10):
    if i not in broken:
        button.add(i)

i = 0
result = ''
for s in str(N):    # N의 각 자리 숫자를 확인하는 for문
    j = 0
    num = int(s)
    while 1:    # 해당 숫자와 가장 가까운 작동하는 번호 찾기
        if num + j in button:
            result += str(num + j)
            break
        elif num - j in button:
            result += str(num - j)
            j *= -1
            break
        j += 1
    i += 1  # 문자열 str(N)의 인덱스
    if j != 0:  # j가 0이 아니라면
        # 뒤에 선택될 수는 j의 값에 따라 모두 가장 큰 번호 or 모두 가장 작은 번호가 선택됨
        m = max(button) if j < 0 else min(button)
        for k in range(i, l):
            result += str(m)
        break

print(min(abs(int(result)-N)+l, abs(100-N)))


# 참고 풀이 - 시간 복잡도가 더 걸리는 거 같은데 ,, 이건 왜 성공!?
import sys

input_data = sys.stdin.readline

N = int(input_data())
M = int(input_data())

if M:
    broken = set(input_data().split())
else:
    broken = set()

result = abs(N-100)
for i in range(1000001):
    for j in str(i):
        if j in broken:     # 해당 숫자를 만들 수 없다면 멈추기
            break
    else:   # 만들 수 있는 번호일 경우
        result = min(result, len(str(i)) + abs(i - N))

print(result)