# 풀이 방법
# 유효기간 문자열을 split 해 날짜로 바꾸기
# 약관 종류 dictionary에 저장 - 조회 시간 단축
# 현재 날짜와 비교해 파기 여부 확인

def solution(today, terms, privacies):
    a, b, c = today.split('.')
    now = (int(a) - 2000) * 28 * 12 + (int(b) - 1) * 28 + int(c)
    terms_dict = dict()
    for term in terms:
        ty, m = term.split(' ')
        terms_dict[ty] = int(m)
    i = 1
    result = []
    for privacy in privacies:
        date, ty = privacy.split(' ')
        a, b, c = date.split('.')
        tmp = (int(a) - 2000) * 28 * 12 + (int(b) + terms_dict[ty] - 1) * 28 + int(c)
        if tmp <= now:
            result.append(i)
        i += 1
    return result