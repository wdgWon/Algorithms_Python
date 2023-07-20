def solution(k, score):
    result = []
    winners = []
    
    for i, s in enumerate(score):
        if(i < k): 
            winners.append(s)
        else:
            winners[0] = max(s, winners[0])
        winners.sort()
        result.append(winners[0])
        
    return result