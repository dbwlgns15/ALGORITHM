def solution(lottos, win_nums):
    answer = [7,7]
    cnt=0
    for i in lottos:
        if i:
            if i in win_nums:
                answer[1]-=1
                answer[0]-=1
        else:
            cnt+=1
    answer[0]-=cnt
    if answer[0]==7:
        answer[0]=6
    if answer[1]==7:
        answer[1]=6
    return answer