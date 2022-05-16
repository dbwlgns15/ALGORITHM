import sys
sys.setrecursionlimit(100000)

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]

max_h = 0
for i in range(n):
    max_h = max(max_h, max(g[i]))

def make_graph(h):
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] >= h:
                graph[i][j] = 1
    return graph

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return 1
    else:
        return 0

answer = 0
for h in range(max_h+1):
    cnt = 0
    graph = make_graph(h)
    for i in range(n):
        for j in range(n):
            if dfs(i,j):
                cnt += 1
    answer = max(answer, cnt)

print(answer)