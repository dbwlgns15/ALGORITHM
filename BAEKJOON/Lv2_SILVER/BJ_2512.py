n = int(input())
m = list(map(int, input().split()))
m.sort()
m.reverse()
money = int(input())

s = sum(m)
if money >= s : 
    ans = m[0]
else:
    i = 1
    s = s - m[0]
    while (money - s)//i < m[i]:
        s -= m[i]
        i += 1
        if i == n:
            break
    ans = (money - s)//(i)

print(ans)