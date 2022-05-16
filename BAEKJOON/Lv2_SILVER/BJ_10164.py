import math

n, m, k = map(int, input().split())

if k:
    x = k % m 
    y = k // m + 1
    if x == 0:
        x = m
        y = k // m
    ans = math.comb(m-x+n-y,m-x) * math.comb(x+y-2,x-1)
    print(ans)
else:
    ans = math.comb(n+m-2,n-1)
    print(ans)