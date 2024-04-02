# n = 100,000 -> 그리디
# 제일 뒤의 집부터 택배 배달, 돌아오면서 가장 많이 수거해오기

# 효율적인 풀이 - 스택!
# stack으로 pop하면서 확인 -> 어떤 지역의 택배 배달, 수거 모두 완료한 경우 다시 지나지 않기 때문
# 현재 deliveries, pickups의 길이 = 이동 거리


def solution(cap, n, deliveries, pickups):
    result = 0
    while deliveries and not deliveries[-1]:  # 방문해야 하는 곳 확인
        deliveries.pop()
    while pickups and not pickups[-1]:
        pickups.pop()

    while deliveries or pickups:
        result += max(len(deliveries), len(pickups)) * 2  # 둘 중 최대 길이 = 이동 거리
        c = cap
        while deliveries:  # 배달해야 하는 곳이 있을 때
            if deliveries[-1] <= c:
                c -= deliveries.pop()
            else:
                deliveries[-1] -= c
                break
        c = cap
        while pickups:  # 수거해야 하는 곳이 있을 때
            if pickups[-1] <= c:
                c -= pickups.pop()
            else:
                pickups[-1] -= c
                break
    return result

