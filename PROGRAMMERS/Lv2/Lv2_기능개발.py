import math
def solution(progresses, speeds):
    p = []
    for i in range(len(speeds)):
        p.append(math.ceil((100-progresses[i])/speeds[i]))
    p.append(1000)
    print(p)
    answer = []
    x = p[0]
    cnt = 0
    for i in p:
        if x == max(x,i):
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            x = max(x,i)

    return answer