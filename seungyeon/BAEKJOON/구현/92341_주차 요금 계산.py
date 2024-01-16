import math
def solution(fees, records):
    answer = dict()
    parking=dict()

    for record in records:
        time,car,status =  record.split(" ")
        hour,minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)

        if status == 'IN':
            parking[car] = minutes
        else:
            try:
                answer[car] += minutes - parking[car]
            except:
                answer[car] = minutes - parking[car]
            del parking[car]
    
    for car,minute in parking.items():
        try:
            answer[car] += 23*60+59 - minute
        except: # 처음일 때
            answer[car] = 23*60+59 - minute

    arr=[]
    for car,time in sorted(list(answer.items()),key=lambda x: x[0]):
        arr.append(fees[1] + math.ceil(max(0, (time - fees[0])) / fees[2]) * fees[3])

    print(arr)

solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])