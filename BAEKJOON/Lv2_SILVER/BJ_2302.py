p_list = [1,1]
for i in range(39):
    a = p_list[i] + p_list[i+1]
    p_list.append(a)
n = int(input())
m = int(input())
m_list = [int(input()) for _ in range(m)]
m_list.append(n+1)

c = 0
chk = []
for i in m_list:
    d = i - c - 1
    c = i
    chk.append(d)

ans = 1
for i in chk:
    ans *= p_list[i]
print(ans)
