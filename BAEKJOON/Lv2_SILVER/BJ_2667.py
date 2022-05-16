n = int(input())
n_map = [list(input()) for _ in range(n)]

def dfs(x,y):
    global m
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    if n_map[x][y] == '1':
        n_map[x][y] = '0'
        m += 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)  
        return 1         
    else:
        return 0
    

cnt = 0
m_list = []
for i in range(n):
    for j in range(n):
        m = 0
        if dfs(i,j):
            cnt += 1
            m_list.append(m)

print(cnt)
m_list.sort()
for i in m_list:
    print(i)