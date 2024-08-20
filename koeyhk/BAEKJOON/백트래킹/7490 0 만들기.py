# N = 9
# 백트래킹 3^8

# 개선한 부분
# eval(ex) 함수를 이용해 식을 문자열로 받아 계산하면 함수 하나를 줄일 수 있다.
# ' ' 부분은 replace로 양옆의 수를 합쳐주기
# 리스트가 아닌 문자열 형태로 3가지 경우의 수 백트래킹 -> pop 필요 x

import sys

input_data = sys.stdin.readline


def bt(x, s):
    if x == N:
        if eval(s.replace(' ', '')) == 0:
            print(s)
        return
    bt(x+1, s+' '+str(num[x]))
    bt(x+1, s+'+'+str(num[x]))
    bt(x+1, s+'-'+str(num[x]))


T = int(input_data())
for _ in range(T):
    N = int(input_data())
    num = [i for i in range(1, N+1)]
    s = str(num[0])
    bt(1, s)
    print()


# 이전 풀이

# 백트래킹으로 숫자 사이에 +, -, ' ' 각각 넣기 -> 총 길이: 2N - 1
# 계산할 때 ' ' 부분 양옆의 숫자는 먼저 더해주고 시작해야 함

# 헷갈렸던 부분
# 숫자를 arr에 append하는 시점 -> 마지막은 따로 더해주기

import sys

input_data = sys.stdin.readline


def bt(x):
    if len(arr) == 2*N-2:
        arr.append(num[x])
        if eval(''.join(map(str, arr)).replace(' ', '')) == 0:
            print(''.join(map(str, arr)))
        arr.pop()
        return
    arr.append(num[x])
    for i in range(x, N-1):
        arr.append(' ')
        bt(i + 1)
        arr.pop()
        arr.append('+')
        bt(i+1)
        arr.pop()
        arr.append('-')
        bt(i+1)
        arr.pop()
    arr.pop()


T = int(input_data())
for _ in range(T):
    N = int(input_data())
    num = [i for i in range(1, N+1)]
    arr = []
    bt(0)
    print()