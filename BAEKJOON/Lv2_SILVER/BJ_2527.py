p_list = [list(map(int, input().split())) for _ in range(4)]

for i in p_list:
    x_1, x_2 = set(range(i[0],i[2]+1)), set(range(i[4],i[6]+1))
    y_1, y_2 = set(range(i[1],i[3]+1)), set(range(i[5],i[7]+1))
    x, y = len(x_1 & x_2), len(y_1 & y_2)
    if x*y == 0:
        print('d')
    elif x*y == 1:
        print('c')
    elif x == 1 and y > 1:
        print('b')
    elif y == 1 and x > 1:
        print('b')
    else:
        print('a')