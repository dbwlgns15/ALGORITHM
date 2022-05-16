score_list = [list(map(int, input().split())) for i in range(5)]
score_sum_list = [sum(score_list[i]) for i in range(len(score_list))]
print(score_sum_list.index(max(score_sum_list))+1,max(score_sum_list))