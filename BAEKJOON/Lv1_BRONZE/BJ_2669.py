plane = [0]*10000

plane_list = [list(map(int, input().split())) for _ in range(4)]

for k in range(4):
    for i in range(plane_list[k][0],plane_list[k][2]):
        for j in range(plane_list[k][1],plane_list[k][3]):
            plane[i*100+j] = 1
print(sum(plane))