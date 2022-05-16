import re
import itertools

text_len = int(input())
text = input()
num_list = re.findall('[0-9]',text)
cal_list = re.findall('[\+\-\*]',text)

per_list = list(itertools.permutations(range(len(cal_list)), len(cal_list)))

ans = []
for idx in per_list:
    idx = list(idx)
    for j in range(len(idx)):
        for k in range(j+1,len(idx)):
            if idx[j] < idx[k]:
                idx[k] -= 1
    # print(idx)

    chk_num = num_list.copy()
    chk_cal = cal_list.copy()
    # print(chk_num)
    # print(chk_cal)
    for i in idx:
        a = eval(f'{chk_num.pop(i)}{chk_cal.pop(i)}{chk_num.pop(i)}')
        chk_num.insert(i,a)
        # print(chk_num)
    ans.append(chk_num[0])
print(max(ans))
