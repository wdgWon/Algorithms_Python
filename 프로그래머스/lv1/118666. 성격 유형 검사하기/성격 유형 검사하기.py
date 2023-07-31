def solution(survey, choices):
    answer = ''
    personality = [char for char in "RTCFJMAN"]
    dic = dict(zip(personality,[0] * 8))
    
    for idx, surv in enumerate(survey):
        a, b = [char for char in surv]
        choice = choices[idx]
        
        if choice <= 3:
            dic[a] += [0,3,2,1][choice]
        elif choice > 4:
            dic[b] += (choice - 4)
            
    for i, a in enumerate(personality[::2]):
        b = personality[i+i+1]
        answer += a if dic[a] >= dic[b] else b
    
    return answer