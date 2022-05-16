b = int(input())
ball_weight = list(map(int, input().split()))
c = int(input())
check_weight = list(map(int, input().split()))

can_check = [ball_weight[0]]
if b > 1:
    for i in ball_weight[1:]:
        a = []
        for j in can_check:
            a += [abs(j+i),abs(j-i),i]
        can_check += a
        can_check = list(set(can_check))

for i in check_weight:
    if i in can_check:
        print('Y', end=' ')
    else:
        print('N', end=' ')