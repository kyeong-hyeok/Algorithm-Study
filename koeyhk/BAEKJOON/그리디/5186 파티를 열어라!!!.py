import sys

input_data = sys.stdin.readline

K = int(input_data())
for j in range(K):
    n, c, l = map(int, input_data().split())
    I, S = dict(), dict()
    for i in range(n):
        r, d = input_data().split()
        r = int(r)
        if d == 'I':    # 술 취한 사람일 경우
            if r in I:
                I[r] += 1
            else:
                I[r] = 1
        else:           # 술 안 취한 사람일 경우
            if r in S:
                S[r] += 1
            else:
                S[r] = 1
    car = [list(map(int, input_data().split())) for _ in range(c)]
    for region, seat in car:
        if region in S and S[region] > 0:       # 해당 지역에 술 안 취한 사람 있을 때
            if region in I and I[region] > 0:   # 해당 지역에 술 취한 사람 있을 때
                if I[region] < seat:            # 좌석보다 술 취한 사람이 적다면
                    seat -= I[region]
                    I[region] = 0
                    if seat > S[region]:        # 남은 좌석보다 술 안 취한 사람이 적다면
                        S[region] = 0
                    elif seat <= S[region]:     # 남은 좌석보다 술 안 취한 사람이 많거나 같다면
                        S[region] -= seat
                else:                           # 좌석보다 술 취한 사람이 많거나 같다면
                    I[region] -= (seat - 1)
                    S[region] -= 1
            else:                               # 해당 지역에 술 취한 사람 없을 때
                if S[region] > seat:            # 좌석보다 술 안 취한 사람이 많다면
                    S[region] -= seat
                else:                           # 좌석보다 술 안 취한 사람이 적거나 같다면
                    S[region] = 0
    print('Data Set '+str(j+1)+':')
    print(sum(I.values()) + sum(S.values()))
