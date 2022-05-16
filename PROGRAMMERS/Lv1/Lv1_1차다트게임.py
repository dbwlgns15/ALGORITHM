import re

dartResult = '1S2D*3T'

cnt_list = re.findall('[0-9]+[SDT][*#]?',dartResult)

for i in range(3):
    a = cnt_list[i]
    cnt_list[i] = [re.findall('[0-9]+',a)[0], re.findall('[SDT]',a)[0]]

    try:
        cnt_list[i].append(re.findall('[*#]',a)[0])
    except:
        pass
    try:
        if cnt_list[i][2] == '*' and i > 0:
            cnt_list[i-1].append('*')
    except:
        pass

for i in range(3):
    n = int(cnt_list[i][0])
    if cnt_list[i][1] == 'S':
        pass
    elif cnt_list[i][1] == 'D':
        n = n**2
    else: 
        n = n**3
    try:
        if cnt_list[i][2] == '*':
            n = n*2
        else:
            n = n*(-1)
    except:
        pass
    try:
        if cnt_list[i][3] == '*':
            n = n*2
    except:
        pass
    
    cnt_list[i] = n

print(sum(cnt_list))
