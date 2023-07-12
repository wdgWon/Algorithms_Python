def solution(n, arr1, arr2):
    r = []
    for i in range(n):
        s = ''
        bin1 = bin(arr1[i])[2:].zfill(n)
        bin2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            s += "#" if (int(bin1[j]), int(bin2[j])) != (0,0) else " "
        r.append(s)
    return r