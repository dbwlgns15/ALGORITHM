n = int(input())
stu_list = [list(map(int, input().split())) for _ in range(n)]
chk_list = [0]*n
for i in range(n):
    for j in range(i+1,n):
        for k in range(5):
            if stu_list[i][k] == stu_list[j][k]:
                chk_list[i] += 1
                chk_list[j] += 1
                break
print(chk_list.index(max(chk_list))+1)
