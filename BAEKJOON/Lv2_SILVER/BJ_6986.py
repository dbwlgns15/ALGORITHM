N, K = map(int, input().split())
pnt = [float(input()) for _ in range(N)]
pnt.sort()
chk = pnt[K:N-K]

a = sum(chk)/len(chk) + 0.00000001
print(f'{a:.2f}')

b = (sum(chk)+chk[0]*K+chk[-1]*K)/N + 0.00000001
print(f'{b:.2f}')