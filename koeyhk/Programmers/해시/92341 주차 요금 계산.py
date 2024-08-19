import math


def solution(fees, records):
    intime = dict()
    parktime = dict()
    for i in records:
        t, num, io = i.split(' ')   # 시간, 차량번호, IN or OUT
        a, b = map(int, t.split(':'))
        t = a*60 + b
        if io == 'IN':      # 입차일 경우
            intime[num] = t
        else:       # 출차일 경우
            pt = t - intime[num]        # 주차 시간
            if int(num) in parktime:    # 이전에 주차 기록이 있는 경우
                parktime[int(num)] += pt
            else:
                parktime[int(num)] = pt
            del intime[num]
    for key, value in intime.items():   # 입차 이후 출차 기록이 없는 경우
        pt = 23*60 + 59 - value
        if int(key) in parktime:
            parktime[int(key)] += pt
        else:
            parktime[int(key)] = pt
    parktime = sorted(parktime.items())
    answer = []
    for key, value in parktime:
        if value < fees[0]:     # 기본 시간보다 적을 경우
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((value-fees[0])/fees[2]) * fees[3])
    return answer