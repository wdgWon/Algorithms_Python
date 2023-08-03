def solution(N, stages):
    stages.sort()
    acc = 0
    
    arr = [{"clear":0,"fail":0} for _ in range(N+2)]
    
    # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
    for stage in stages:
        arr[stage]["fail"] += 1
    
    # 스테이지에 도달한 플레이어 수
    for stage in arr[::-1]:
        acc += stage["fail"]
        stage["clear"] += acc
    
    # 실패율 기준 정렬
    sort = [x for x in range(1, N+1)]
    
    return sorted(sort, 
                  key=lambda stage: 
                  (arr[stage]["fail"] / arr[stage]["clear"] 
                  if arr[stage]["clear"] > 0 else 0), 
                  reverse=True )