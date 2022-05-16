dice_count = int(input())
dice_list = [list(map(int, input().split())) for _ in range(dice_count)]
p = {0:5, 5:0, 1:3, 3:1, 2:4, 4:2}
max_a = 0
for i in range(6):
    a = dice_list[0][i]
    max_sum = 0 
    for j in range(dice_count):
        a_index = dice_list[j].index(a)
        b_index = p[a_index]
        a = dice_list[j][b_index]
        if a == 6 or dice_list[j][a_index] == 6:
            if dice_list[j][a_index] + a == 11:
                max_sum += 4
            else:
                max_sum += 5
        else:
            max_sum += 6
    if max_a < max_sum:
        max_a = max_sum
print(max_a)




    