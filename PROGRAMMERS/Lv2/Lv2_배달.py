from collections import deque
def solution(N, road, K):
    road_dict = {}
    for i in road:
        if road_dict.get(tuple(sorted(i[:2]))):
            road_dict[tuple(sorted(i[:2]))] = min(road_dict[tuple(sorted(i[:2]))], i[2])
        else:
            road_dict[tuple(sorted(i[:2]))] = i[2]

    graph = [ [] for _ in range (N+1) ]

    for i in road_dict:
        graph[i[0]].append((i[1],road_dict[i]))
        graph[i[1]].append((i[0],road_dict[i]))

    visited = [-1] * (N+1)

    def bfs(graph,start,visited):
        dq = deque([start])
        visited[start[0]] = start[1]
        l = start[1]
        while dq:
            a = dq.popleft()
            for i in graph[a[0]]:
                l = visited[a[0]]
                if visited[i[0]] == -1:
                    dq.append(i)
                    visited[i[0]] = l + i[1]
                else:
                    if visited[i[0]] > l + i[1]:
                        dq.append(i)
                        visited[i[0]] = min(visited[i[0]],l + i[1])
    bfs(graph,(1,0),visited)

    answer = 0
    for i in visited[1:]:
        if i <= K:
            answer += 1
    return answer