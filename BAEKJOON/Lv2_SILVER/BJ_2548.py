n = int(input())
n_list = list(map(int, input().split()))
l = len(n_list)
chk = 0
a = 0
chk_list = []
for i in range(min(n_list)-1,max(n_list)):
    if i in n_list:
        a += n_list.count(i)
        chk += (a*2 - l)
        chk_list.append(chk)
    else:
        chk += (a*2 - l)
        chk_list.append(chk)
x = chk_list.index(min(chk_list))
print(min(n_list)+x)

