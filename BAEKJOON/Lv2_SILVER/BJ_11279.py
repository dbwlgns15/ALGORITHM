import heapq
import sys

n = int(input())

hq=[]

for _ in range(n):
    i = int(sys.stdin.readline())
    if i:
        heapq.heappush(hq,(-i,i))
    else:
        if len(hq):
            print(heapq.heappop(hq)[1])
        else:
            print(i)