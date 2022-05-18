import re
def solution(replies, n, k):
    answer = []
    for reply in replies:
        chk = 1
        for i in range(n,(len(reply)//k)+1):
            chk_re = '([A-F]{'+str(i)+'})'+'\\1'*(k-1)
            chk_list = re.findall(chk_re,reply)
            if chk_list:
                chk = 0
        answer.append(chk)
    return answer