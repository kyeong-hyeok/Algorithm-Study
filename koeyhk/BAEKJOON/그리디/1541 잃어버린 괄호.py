# 탐욕법
# -로 split한 후 다 빼주면 최솟값을 만족!

# 놓쳤던 부분
# 1. -, + 둘다로 구분해서 나눈 후 답을 구해야 한다고 생각함
# -> -로 split한 후, +가 있는 값들은 모두 더하고 result에서 해당 값을 빼주면 된다.

import sys

input_data = sys.stdin.readline
equ = input_data().rstrip().split('-')
first = 1
for e in equ:
    tmp = e.split('+')
    t = 0
    for i in tmp:
        t += int(i)
    if first:
        result = t
        first = 0
    else:
        result -= t

print(result)


# 이전 풀이 -> 복잡

# 0~9, + -, ()
# ()를 적절히 쳐서 값 최소로 만들기
# N = 50
# 1 + 1 - 2 - (3 + 5)
# 1 - 1 - 2 - 5 + 5

import sys

input_data = sys.stdin.readline
equ = input_data().rstrip()
eq = []
s, e = 0, -1
for i in range(len(equ)):
    if equ[i] == '+' or equ[i] == '-':
        eq.append(int(equ[s:e+1]))
        eq.append(equ[i])
        s = i + 1
        e = i
    else:
        e += 1
        if i == len(equ)-1:
            eq.append(int(equ[s:e+1]))
result = eq[0]
i = 1
prev = 1
tmp = 0
while i < len(eq):
    if eq[i] == '+':
        tmp += eq[i+1]
        if prev == 1:
            result += tmp
            tmp = 0
        i += 2
    elif eq[i] == '-':
        if prev == 1:
            prev = -1
            tmp = eq[i+1]
        elif prev == -1:
            result -= tmp
            tmp = eq[i+1]
        i += 2

result += prev * tmp
print(result)