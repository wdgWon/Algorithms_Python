def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # state 배열에 각 학생의 도난 여부 저장
    state = [i not in lost for i in range(0, n+1)]

    for pair in reserve:
        # 해당 학생이 빌려줄 수 있는 상태
        if state[pair]:
            # 앞 학생이 체육복을 필요로 하는지 확인
            if pair > 1 and not state[pair-1]:
                state[pair-1] = True
            # 뒷 학생이 체육복을 필요로 하는지 확인
            elif pair < n and not state[pair+1]:
                # 도난 당했는데 체육복 여벌이 있으면 그거 본인이 입어야됨
                if pair+1 not in reserve:
                    state[pair+1] = True
        # 빌려줄 수 없는 상태
        else:
            state[pair] = True

    return sum(state[1:])