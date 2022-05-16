import sys
n,p,q = map(int,sys.stdin.readline().split())

a = {}

def sol(i,p,q):
    if i == 0:
        return 1
    if a.get(i):
        return a[i]
    a[i] = sol(int(i/p),p,q) + sol(int(i/q),p,q)
    return a[i]

print(sol(n,p,q))
