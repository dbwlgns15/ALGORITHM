n = input()

first_n = n

cnt = 0 
while True:
    if len(n) == 1:
        n = str(int(n*2))
        cnt += 1 
    else:
        n2 = str(int(n[0])+int(n[1]))
        n = str(int(n[-1] + n2[-1]))
        cnt += 1
    if first_n == n:
        print(cnt)
        break