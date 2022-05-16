def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d:
        budget = budget - i
        if budget >= 0:
            cnt += 1
        else:
            break

    return cnt