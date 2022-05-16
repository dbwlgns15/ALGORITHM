w = 8
h = 12

def gcd(x,y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)
g = gcd(w, h)

print(w*h-w-h+g)

