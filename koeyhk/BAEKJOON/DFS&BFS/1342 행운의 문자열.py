def lucky(word, l):
    if l == len(S):     # 행운의 문자열
        return 1
    result = 0
    for k in c.keys():      # 단어 확인
        if word != k and c[k] != 0:     # 이전 단어와 같지 않고 단어의 개수가 0이 아닐 때
            c[k] -= 1       # 단어 개수 줄이기
            result += lucky(k, l+1)     # l+1로 함수 호출
            c[k] += 1       # 단어 개수 늘리기
    return result


S = input()
c = dict()
for i in S:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print(lucky('', 0))