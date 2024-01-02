# 처음 접근
# 각 열의 각 행마다 둘 수 있는지 확인? -> 시간 초과

# 접근 방법
# 직접 퀸을 행, 열에 대입해 조건 파악
# 한 행에 하나의 퀸이 존재해야 함!

# 1. x행 i열에 퀸을 놓았을 때 해당 열과 해당 행에는 퀸을 놓을 수 없음
# 해당 행, 열에 퀸이 있는지 여부를 확인할 수 있어야 함
# -> row[x] = i 라면 x행 i열 퀸 존재

# 2. x행 i열에 퀸을 놓았을 때 대각선에 퀸을 놓을 수 없음
# 대각선에 퀸이 있는지 여부를 확인할 수 있어야 함
# -> abs(row[x]-row[i]) == x-i 라면 대각선에 퀸 존재

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return 0
    return 1


def bt(x):
    global result
    if x == N:
        result += 1
        return
    # 각 행에 퀸 놓기
    for i in range(N):
        row[x] = i
        if check(x):
            bt(x+1)


N = int(input())
result = 0
row = [0] * N

bt(0)
print(result)