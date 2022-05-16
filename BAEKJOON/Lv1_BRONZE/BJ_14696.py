round_count = int(input())

for _ in range(round_count):
    
    a = list(map(int, input().split()))[1:]
    a.sort()
    a.reverse()
   
    b = list(map(int, input().split()))[1:]
    b.sort()
    b.reverse()

    if a > b:
        print('A')
    elif b > a:
        print('B')
    else:
        print('D')