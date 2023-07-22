def solution(k, m, score):
    frequency = {}
    remind = 0
    count = 0
    
    for num in score:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    for key, value in sorted(frequency.items(), reverse=True):
        q, r = divmod(value, m)
        if remind + r >= m:
            q += 1
        count += q * key * m
        remind = (remind + r) % m
    return count