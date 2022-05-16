x, y = map(int, input().split())
n = int(input())
point_list = [list(map(int, input().split())) for _ in range(n+1)]

new_list = []
for i in point_list:
    if i[0] == 1:
        a = [1,i[1],y]
    elif i[0] == 2:
        a = [3,i[1],0]
    elif i[0] == 3:
        a = [2,0,y-i[1]]
    else:
        a = [4,x,y-i[1]]
    new_list.append(a)
d = new_list.pop()

ans = 0
for i in new_list:
    if abs(i[0] - d[0]) == 2:
        if d[0]%2 == 1:
            ans += y + min(i[1]+d[1],2*x-i[1]-d[1])
        else:
            ans += x + min(i[2]+d[2],2*y-i[2]-d[2])
    else:
        ans += abs(i[1]-d[1]) + abs(i[2]-d[2]) 
print(ans)