def solution(id_list, report, k):
    dic = dict(map(lambda x: [x, [0,{}]], id_list))
    
    for r in report:
        s, r = r.split(" ")
        if r not in dic[s][1]:
            dic[r][0] += 1
            dic[s][1][r] = True
            
    def counter(id):
        count = 0
        for r in dic[id][1]:
            if(dic[r][0] >= k):
                count += 1
        return count
    
    return list(map(counter, id_list))