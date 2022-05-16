n,m = map(int, input().split())

def gcd(x,y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)

print(gcd(n,m))
print(int(n*m/gcd(n,m)))