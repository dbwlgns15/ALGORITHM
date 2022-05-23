import itertools

N = int(input())
n_list = list(map(int, input().split()))
c_ = list(map(int, input().split()))
c = ['+','-','*','//']

cal_list = []
for i in range(4):
    cal_list += [c[i]] * c_[i]
all_cal_list = itertools.permutations(cal_list, N-1)
all_cal_list = list(set(all_cal_list))

answer_list = []
for i in all_cal_list:
    answer = n_list[0]
    for j in range(len(i)):
        if i[j] == '//':
            if answer < 0:
                answer = -eval(str(-answer) + i[j] + str(n_list[j+1]))
            else:
                answer = eval(str(answer) + i[j] + str(n_list[j+1]))
        else:
            answer = eval(str(answer) + i[j] + str(n_list[j+1]))
    answer_list.append(answer)
print(max(answer_list),min(answer_list),sep='\n')