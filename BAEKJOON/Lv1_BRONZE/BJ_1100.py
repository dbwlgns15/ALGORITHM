chess_list = [input() for i in range(8)]
F_count = 0
for i in range(len(chess_list)):
    for j in range(len(chess_list[i])):
        if j%2 == i%2 and chess_list[i][j] == 'F':
                F_count += 1
print(F_count)