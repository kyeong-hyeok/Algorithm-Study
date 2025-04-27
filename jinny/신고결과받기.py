def solution(id_list, report, k):
    report = set(report)
    dict = {}
    for i in report:
        nm=i.split()
        if nm[0] in dict:
            dict[nm[0]] +=[nm[1]]
        else:
            dict[nm[0]] = [nm[1]]
            
    #print(dict)
    
    value_dic = []
    for i in dict.values():
        value_dic +=i

    #print(value_dic)
    
    stop_value = []
    for i in id_list:
        if i in value_dic:
            if value_dic.count(i) >= 2:
                stop_value += [i]

    #print(stop_value)

    answer = []
    for i in id_list:
        if i in dict.keys():
            #print("몰라"+i)
            count = 0
            for j in dict[i]:
                if j in stop_value:
                    count+=1
            answer.append(count)
        else :
            answer.append(0)
    return answer       
def main():
    # 입력 예시
    id_list_1 = ["muzi", "frodo", "apeach", "neo"]
    report_1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k_1 = 2
    
    id_list_2 = ["con", "ryan"]
    report_2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k_2 = 3
    
    # 결과 출력
    print(solution(id_list_1, report_1, k_1))  # [2, 1, 1, 0]
    print(solution(id_list_2, report_2, k_2))  # [0, 0]

if __name__ == "__main__":
    main()
