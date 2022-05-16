n = int(input())
ans = 0
for a in range(1,n):
    for b in range(a,n-a):
        c = n - a - b
        if a <= b <= c and a + b > c:
            ans += 1
        if (a <= b <= c) is False:
            break
print(ans)