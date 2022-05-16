num = int(input())
b=0
for i in range(1,num+1):
    a=[num]
    a.append(i)
    j = 1
    while a[j-1] - a[j] >= 0:
        a.append(a[j-1] - a[j])
        j += 1
    if len(a) > b:
        b = len(a)
        max_list = a
print(len(max_list))
for i in max_list:
    print(i, end=' ')