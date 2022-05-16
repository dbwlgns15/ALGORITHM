N, M = map(int,input().split())
name_dict = {}
for _ in range(N):
    name1 = input()
    name_dict[name1] = 1
for _ in range(M):
    name2 = input()
    if name_dict.get(name2) == None:
        name_dict[name2] = 1
    else:
        name_dict[name2] += 1
count_2 = 0
list_2 = []
for i in name_dict:
    if name_dict[i] == 2:
        count_2 += 1
        list_2.append(i)
print(count_2)
list_2.sort()
for i in list_2:
    print(i)
