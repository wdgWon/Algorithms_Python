from string import ascii_uppercase
def solution(msg):
    D = {k:v for v,k in enumerate(ascii_uppercase)}
    cnt = 26
    output = []
    while msg:
        for length in reversed(range(1,len(msg)+1)):
            if msg[:length] in D:
                if msg[:length+1] not in D:
                    D[msg[:length+1]] = cnt
                output.append(D[msg[:length]]+1)
                msg = msg[length:]
                cnt += 1
                break
        
    return output