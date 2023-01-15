# 2023 KAKAO BLIND RECRUITMENT
# Lv 1. 개인정보 수집 유효기간

# 13:34 시작 14:02 끝


def solution(today, terms, privacies):
    answer = []
    t_dict = {}
    for term in terms:
        key, value = term.split()
        t_dict[key] = value
    #print(t_dict)
    
    n_year, n_mon, n_day = map(int, today.split('.'))
    
    idx = 1
    for privacy in privacies:
        p_date, p_term = privacy.split()
        add_mon = int(t_dict[p_term])
        
        p_year, p_mon, p_day = map(int, p_date.split('.')) # 나눠서 저장

        #print(type(add_mon))
        #print(type(p_mon))
        p_mon += add_mon
        # print(p_mon)
        while p_mon > 12:
            p_mon -= 12
            p_year += 1
        
        #print(n_year, n_mon, n_day)
        #print(p_year, p_mon, p_day)
        
        # today와 비교 (today보다 이전일 경우 파기해야 함)
        if p_year < n_year: # today 이전 연도
            answer.append(idx)
        elif p_year == n_year: # today 연도 같음
            if p_mon < n_mon: # today 이전 월
                answer.append(idx)
            elif p_mon == n_mon: # today 월 같음
                if p_day <= n_day: # today 이전 일
                    answer.append(idx)

        idx+=1


    return answer