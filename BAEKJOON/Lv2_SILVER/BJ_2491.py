n = int(input())
n_list = list(map(int, input().split()))
ans = 0
i = 0
while i < n-2:
    x = 0
    while n_list[i] <= n_list[i+1]:
        i += 1
        x += 1
        if ans < x:
            ans = x
        if i == n-1:
            break
    i += 1
i = 0
while i < n-2:
    x = 0
    while n_list[i] >= n_list[i+1]:
        i += 1
        x += 1
        if ans < x:
            ans = x
        if i == n-1:
            break
    i += 1
print(ans+1)