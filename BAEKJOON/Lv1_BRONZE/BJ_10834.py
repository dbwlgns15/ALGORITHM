cnt = int(input())
belt = [list(map(int,input().split())) for _ in range(cnt)]
a, b, c = 1, 1, 0
for i in belt:
    a *= i[0]
    b *= i[1]
    c += i[2]
print(c%2,int(b/a))