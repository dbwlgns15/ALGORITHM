n = int(input().replace(' ',''))
def find(n):
    n = str(n)
    n_list = [n[i-4]+n[i-3]+n[i-2]+n[i-1] for i in range(4)]
    m = int(min(n_list))
    return(m)

ans = 1
for i in range(1111,find(n)):
    a, b, c, d = map(int, str(i))
    if b!=0 and c!=0 and d!=0 and i == find(i):
        ans += 1
print(ans)