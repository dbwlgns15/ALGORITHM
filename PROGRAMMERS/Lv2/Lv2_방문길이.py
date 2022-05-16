def solution(dirs):
    road_list =[ [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]] for _ in range(11) ]
    x, y = 5, 5
    for i in dirs:
        if i == 'U':
            if 0 <= y <= 9:
                road_list[x][y][0] = 1
                y += 1
        elif i == 'R':
            if 0 <= x <= 9:
                road_list[x][y][1] = 1
                x += 1
        elif i == 'D':
            if 1 <= y <= 10:
                y -= 1
                road_list[x][y][0] = 1
        elif i == 'L':
            if 1 <= x <= 10:
                x -= 1
                road_list[x][y][1] = 1

    answer = 0
    for i in road_list:
        for j in i:
            answer += sum(j)
    return answer