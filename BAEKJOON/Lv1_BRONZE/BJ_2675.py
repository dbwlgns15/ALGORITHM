test_time=int(input())
for i in range(test_time):
    list_RS = input().split()
    R = int(list_RS[0])
    S = list_RS[1]
    for j in S:
        print(j * R, end='')
    print('')