stone = [list(map(int, input().split())) for _ in range(19)]

x = [1, 0, 1, -1]
y = [0, 1, 1, 1]
chk =0
for i in range(19):
    for j in range(19):
        if stone[i][j]:
            color = stone[i][j]
            for d in range(4):
                cnt = 1
                ix, jy = i+x[d], j+y[d]
                while 0<=ix<=18 and 0<=jy<=18 and color == stone[ix][jy]:
                    cnt += 1
                    if cnt == 5:
                        if 0<=i-x[d]<=18 and 0<=j-y[d]<=18 and color == stone[i-x[d]][j-y[d]]:
                            break
                        if 0<=ix+x[d]<=18 and 0<=jy+y[d]<=18 and color == stone[ix+x[d]][jy+y[d]]:
                            break
                        print(color)
                        print(i+1,j+1)
                        chk = 1
                    ix += x[d]
                    jy += y[d]
if chk == 0:
    print(0)

