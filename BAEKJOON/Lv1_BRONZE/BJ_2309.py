height_list = [int(input()) for i in range(9)]
height_list.sort()

for i in range(9):
    for j in range(i+1,9):
        if sum(height_list) - height_list[i] - height_list[j] == 100:
            x = height_list[i]
            y = height_list[j]

height_list.remove(x)
height_list.remove(y)

for i in height_list:
    print(i)