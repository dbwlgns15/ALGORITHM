c, r = map(int, input().split())
k = int(input())

if c * r < k :
    print(0)
else:
    t = 1
    while k > 2*c + 2*r + 4 - 8*t :
        k -= 2*c + 2*r + 4 - 8*t
        t += 1
    c_ = c - 2*t + 1
    r_ = r - 2*t + 1
    if r_ >= k > 0:
        x = 0
        y = k - 1
    elif r_ + c_ >= k > r_:
        x = k - r_ - 1
        y = r_
    elif 2*r_ + c_ >= k > r_ + c_:
        x = c_
        y = 2*r_ + c_ + 1 - k
    else:
        x = 2*c_ + 2*r_ - k + 1
        y = 0
    print(t+x, t+y)