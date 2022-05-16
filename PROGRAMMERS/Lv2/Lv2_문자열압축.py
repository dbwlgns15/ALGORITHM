import re
def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        result = len(s)
        x = '[a-z]{'+str(i)+'}'
        word_list = re.findall(x,s)
        cnt = 1
        cnt_list = []
        for j in range(1,len(word_list)):
            if word_list[j] == word_list[j-1]:
                cnt+=1
            else:
                cnt_list.append(cnt)
                cnt=1
        cnt_list.append(cnt)
        cnt_list = [cnt for cnt in cnt_list if cnt != 1] 
        cnt_len = 0
        for k in cnt_list:
            cnt_len += len(str(k))
        result = result - (sum(cnt_list)-len(cnt_list))*i + cnt_len
        answer = min(answer,result)
    return answer