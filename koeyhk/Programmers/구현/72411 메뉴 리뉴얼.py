from itertools import combinations
import collections


def solution(orders, course):
    result = []
    order_list = []
    for order in orders:
        order = sorted(order)
        for c in course:
            order_list += combinations(order, c)
    max_count = collections.Counter(order_list).most_common()
    check = dict()
    for o, count in max_count:
        if len(o) not in check.keys() or check[len(o)] == count:
            if count <= 1:
                break
            result.append(''.join(o))
            check[len(o)] = count
    return sorted(result)

