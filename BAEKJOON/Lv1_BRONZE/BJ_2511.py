a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_score = 0
b_score = 0

for i in range(10):
    if a[i] > b[i]:
        a_score += 3
    elif a[i] < b[i]:
        b_score += 3
    else:
        a_score += 1
        b_score += 1

print(a_score, b_score)
if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
else:
    i = 9
    while a[i] == b[i] and i > 0:
        i -= 1
    if a[i] > b[i]:
        print('A')
    elif a[i] < b[i]:
        print('B')
    else:
        print('D')