test_time = int(input())

for i in range(test_time):
    a,b = map(int, input().split())
    print('Case #{}: '.format(i+1), end='')
    print(a+b)