n = int(input())
stu_count = int(input())
stu_list = list(map(int, input().split()))
stu_dict = {}
for i in stu_list:
    if len(stu_dict) < n:
        if stu_dict.get(i) is None:
            stu_dict[i] = 1
        else:
            stu_dict[i] += 1
    else:
        if stu_dict.get(i):
            stu_dict[i] += 1
        else:
            del stu_dict[list(stu_dict.keys())[list(stu_dict.values()).index(min(stu_dict.values()))]]
            stu_dict[i] = 1

for i in sorted(list(stu_dict.keys())):
    print(i, end=' ')