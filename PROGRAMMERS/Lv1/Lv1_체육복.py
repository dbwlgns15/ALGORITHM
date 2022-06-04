def solution(n, lost, reserve):
    a = set(lost)&set(reserve)
    lost = set(lost) - a
    reserve = set(reserve) - a
    cnt = 0
    for i in range(1,n+1):
        if i in lost:
            if i-1 in reserve:
                cnt += 1
                reserve -= {i-1}
            elif i+1 in reserve:
                cnt += 1
                reserve -= {i+1}
            else:
                pass
        else:
            cnt += 1
            
    return cnt