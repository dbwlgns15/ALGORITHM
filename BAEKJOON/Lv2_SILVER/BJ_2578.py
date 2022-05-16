bingo = []
for _ in range(5):
    bingo += list(map(int,input().split()))

num = []
for _ in range(5):
    num += list(map(int,input().split()))

check_a = [[i*5-j-1 for j in range(5)]for i in range(1,6)]
check_b = [[5*i-5+j for i in range(1,6)] for j in range(5)]
check_c = [[0,6,12,18,24],[4,8,12,16,20]]
check_list = check_a + check_b + check_c

for index, i in enumerate(num):
    bingo[bingo.index(i)] = 0
    ans = 0
    for j in check_list:
        if sum([bingo[k] for k in j]) == 0:
            ans += 1
        if ans == 3:
            print(index+1)
            break
    if ans == 3:
        break   