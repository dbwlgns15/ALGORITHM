from collections import Counter
def solution(N, stages):
    answer = []
    cnt = Counter(stages)
    l = len(stages)
    w_list = []
    w_dict = {}
    for i in range(N):
        if l:
            p = cnt.get(i+1,0)
            w = p/l
            l -= p
            w_list.append(w)
            if w_dict.get(w):
                w_dict[w] += [i+1]
            else:
                w_dict[w] = [i+1]
        else:
            w = 0
            w_list.append(w)
            if w_dict.get(w):
                w_dict[w] += [i+1]
            else:
                w_dict[w] = [i+1]

    w_list = sorted(list(set(w_list)))
    for i in range(len(w_list)):
        answer += w_dict[w_list.pop()]

    return answer