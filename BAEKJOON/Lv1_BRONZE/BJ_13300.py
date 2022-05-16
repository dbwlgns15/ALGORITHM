stu_count, stu_max = map(int, input().split())

total_list = [[0, 0] for _ in range(6)] 
for _ in range(stu_count):
    stu_sex, stu_grade = map(int, input().split())
    total_list[stu_grade-1][stu_sex] += 1

room_count = 0
for i in total_list:
    room_count += i[1]//stu_max
    room_count += i[0]//stu_max
    if not i[1] % stu_max == 0:
        room_count += 1
    if not i[0] % stu_max == 0:
        room_count += 1
print(room_count)
