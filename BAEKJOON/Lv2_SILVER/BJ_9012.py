import re

n = int(input())
txt = [input() for _ in range(n)]

for a in txt:
    
    while a:
        b = re.sub('\([^()]*\)','',a)
        if a == b:
            break
        a = b
    if a:
        print('NO')
    else:
        print('YES')
