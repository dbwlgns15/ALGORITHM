import heapq
def solution(A, B):
    heapq.heapify(A)
    heapq.heapify(B)

    answer = 0
    for _ in range(len(A)):
        min_a = heapq.heappop(A)
        if len(B) == 0:
            break
        min_b = heapq.heappop(B)
        while min_a >= min_b:
            if len(B) == 0:
                answer -= 1
                break
            else:
                min_b = heapq.heappop(B)
        answer += 1

    return answer
