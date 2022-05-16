import re
def solution(rooms, target):
    room_dict = {}
    for i in rooms:
        n = re.findall('[0-9]+',i)[0]
        m = re.findall('[a-zA-Z]+',i)
        for j in m:
            if room_dict.get(j):
                room_dict[j] += [n]
            else:
                room_dict[j] = [n]
                
    nl_list = []
    for i in room_dict:
        l = 10000
        m = len(room_dict[i])
        for j in room_dict[i]:
            l = min(l,abs(target-int(j)))
        nl_list.append([m,l,i])
    nl_list.sort()

    answer = []
    for i in nl_list:
        if i[1]:
            answer.append(i[2])
    return answer