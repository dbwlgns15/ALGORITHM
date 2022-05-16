import heapq
import sys

n = int(input())

hq = []
heapq.heapify(hq)

for _ in range(n):
    i = int(sys.stdin.readline())
    if i == 0:
        if len(hq) > 0:
            print(heapq.heappop(hq))
        else:
            print('0')
    else:
        heapq.heappush(hq,i)
