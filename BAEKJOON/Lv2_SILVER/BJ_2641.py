n = int(input())
a = list(map(int, input().split()))
reverse_dict = {1:3,2:4,3:1,4:2}
b = list(map(lambda x: reverse_dict[x], a))[::-1]

a_list = []
for i in range(n):
    x = [ a[i+j-n] for j in range(n) ]
    y = [ b[i+j-n] for j in range(n) ]
    a_list.append(x)
    a_list.append(y)

n = int(input())
cnt = 0
chk = []
for _ in range(n):
    c = list(map(int, input().split()))
    if c in a_list:
        cnt += 1
        chk.append(c)
print(cnt)
for i in chk:
    print(' '.join(map(str,i)))


