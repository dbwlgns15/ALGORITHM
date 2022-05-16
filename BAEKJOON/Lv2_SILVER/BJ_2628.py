a, b = map(int, input().split())
cut = int(input())
cut_list = [list(map(int, input().split())) for _ in range(cut)]

a_list = [i[1] for i in cut_list if i[0] == 1]
a_list += [0,a]
a_list.sort()
b_list = [i[1] for i in cut_list if i[0] == 0]
b_list += [0,b]
b_list.sort()

a_list2 = [a_list[i]-a_list[i-1] for i in range(1,len(a_list))]
b_list2 = [b_list[i]-b_list[i-1] for i in range(1,len(b_list))]

print(max(a_list2)*max(b_list2))