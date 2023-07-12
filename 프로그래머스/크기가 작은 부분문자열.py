def solution(t, p):
    # c = list(filter(lambda x: int(x) <= int(p), (t[i:i+len(p)] for i in range(0, len(t)-len(p)+1))))
    # print(c)
    pl = len(p)
    tl = len(t)
    c = [t[i:i+pl] for i in range(0, tl-pl+1) if int(t[i:i+pl]) <= int(p)]
    return len(c)