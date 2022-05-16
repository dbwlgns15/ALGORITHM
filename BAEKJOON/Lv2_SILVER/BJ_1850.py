n, m = map(int, input().split())

def gcd(x,y):
    if x > y:
        x, y = y, x
    if y % x == 0:
        return x
    else:
        return gcd(x, y % x)

print('1'*gcd(n,m))