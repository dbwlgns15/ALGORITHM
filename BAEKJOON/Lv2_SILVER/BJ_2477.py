cham_count = int(input())
way_long = [list(map(int, input().split())) for _ in range(6)]
way_list = [way_long[i][0] for i in range(6)]
max_map = 1
min_map = 1
for i in range(1,5):
    if way_list.count(i) == 1:
        max_map = max_map * way_long[way_list.index(i)][1]
        min_map = min_map * way_long[way_list.index(i)-3][1]
print(cham_count * (max_map - min_map))