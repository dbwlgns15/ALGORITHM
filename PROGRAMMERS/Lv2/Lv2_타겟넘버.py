from collections import deque
def solution(numbers, target):
    answer = 0
    dq = deque([(-1,0)])
    while dq:
        a = dq.popleft()
        if a[0] == len(numbers)-1:
            if a[1] == target:
                answer += 1
            continue
        dq.append((a[0]+1,a[1]+numbers[a[0]+1]))
        dq.append((a[0]+1,a[1]-numbers[a[0]+1])) 
    return answer