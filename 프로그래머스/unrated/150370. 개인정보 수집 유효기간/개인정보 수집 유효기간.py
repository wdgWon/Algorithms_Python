def solution(today, terms, privacies):
    t_year, t_month, t_day = list(map(int, today.split(".")))
    terms = dict(map(lambda s: s.split(" "), terms))
    
    expire = []
    
    for idx, privacy in enumerate(privacies):
        time, term = privacy.split(" ")
        p_year, p_month, p_day = list(map(int, time.split(".")))
        
        day = t_day - p_day
        month = (t_month - p_month) * 28
        year = (t_year - p_year) * 336
        
        remain = year + month + day
        term = int(terms[term]) * 28
        
        if term - remain <= 0:
            expire.append(idx + 1)
        
    
    return expire
