from itertools import product


def solution(users, emoticons):
    answer = []
    discount = [10, 20, 30, 40]
    for case in product(discount, repeat=len(emoticons)):   # 이모티콘마다 할인율 적용
        result = [0, 0]
        for u in users:
            cost = 0
            for i, dis in enumerate(case):  # 인덱스와 원소 동시 접근
                if dis >= u[0]:
                    cost += emoticons[i] * (100 - dis) // 100
            if cost >= u[1]:    # 예산 초과 시
                result[0] += 1
            else:
                result[1] += cost
        answer.append(result)

    answer.sort(key=lambda x: (-x[0], -x[1]))   # 가입자 최대, 판매액 최대 정렬
    return answer[0]