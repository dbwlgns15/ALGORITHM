w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = ((t % (2*w)) + p) % (2*w)
y = ((t % (2*h)) + q) % (2*h)
if x > w:
    x = w*2 - x
if y > h:
    y = h*2 - y
print(x, y)