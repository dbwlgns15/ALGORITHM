from collections import deque
def solution(priorities, location):
    dq = deque(priorities)
    if len(dq) == 1:
        return 1
    cnt = 0
    m = max(dq)
    while dq:
        x = dq.popleft()
        if len(dq) == 0:
            return cnt+1
        location -= 1
        if x == m:
            cnt += 1
            m = max(dq)
            if location == -1:
                return cnt
        else:
            dq.append(x)
            if location == -1:
                location = len(dq)-1