test_time = int(input())

for i in range(test_time):
    a,b = map(int, input().split())
    print('Case #{0}: {1} + {2} = {3}'.format(i+1,a,b,a+b))