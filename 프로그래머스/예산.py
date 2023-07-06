def solution(d, budget):
    d.sort()
    c = 0
    
    for idx, price in enumerate(d):
        if c + price <= budget:
            c += price
        else: return idx
    return len(d)