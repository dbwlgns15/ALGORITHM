import re

n = int(input())
ol = input()

ol_list = [list(i) for i in re.findall('[01]{6}',ol)]
a = ['000000','001111','010011','011100','100110','101001','110101','111010']
a = [tuple(i) for i in a]
check_dict = {a[0]:'A',a[1]:'B',a[2]:'C',a[3]:'D',a[4]:'E',a[5]:'F',a[6]:'G',a[7]:'H'}

answer = ''
for i in ol_list:
    cnt = 0
    if check_dict.get(tuple(i)):
        answer += check_dict.get(tuple(i))
    else:  
        for j in range(6):
            chk = i.copy()
            if chk[j] == '0':
                chk[j] = '1'
            else:
                chk[j] = "0"
            if check_dict.get(tuple(chk)):
                answer += check_dict.get(tuple(chk))
                break
            else:
                cnt += 1
        if cnt == 6:
            print(ol_list.index(i)+1)
            break

if cnt != 6:
    print(answer)