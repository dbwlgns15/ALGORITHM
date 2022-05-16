import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    m1 = heapq.heappop(scoville)
    answer = 0
    while m1 < K:
        if len(scoville) == 0:
            return -1
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville,m1+(m2*2))
        m1 = heapq.heappop(scoville)
        answer += 1
    return answer