def solution(n, m):
    (min_num, max_num) = (n, m) if n < m else (m, n)
    gcm, i = 0, 1
    measure_min = set()

    # min 의 약수 찾기
    for num in range(1,int(min_num**0.5)+2):
        if(min_num % num == 0):
            measure_min.update([num, min_num // num])

    # min 의 약수에서 최대공약수 찾기
    if(max_num % min_num):
        for measure in measure_min:
            if(max_num % measure == 0):
                gcm = max(measure, gcm)
    else:
        gcm = min_num

    # 최소공배수 찾기
    while (max_num * i) % min_num:
        i += 1
    lcm = max_num * i

    return [gcm, lcm]