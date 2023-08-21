def solution(numLog):
    result = ''
    for idx, num in enumerate(numLog):
        if(idx == 0):
            continue
        w = num - numLog[idx-1]
        if w == 1:
            result += "w"
        elif w == -1:
            result += "s"
        elif w == 10:
            result += "d"
        else:
            result += "a"
    
    return result
        