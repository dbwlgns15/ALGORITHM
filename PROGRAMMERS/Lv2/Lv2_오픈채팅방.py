def solution(record):
    id_dict = {}
    answer = []
    for i in record:
        a = i.split()
        if a[0] == 'Enter':
            answer.append(f'{a[1]}님이 들어왔습니다.')
            id_dict[a[1]] = a[2]
        elif a[0] == 'Leave':
            answer.append(f'{a[1]}님이 나갔습니다.')
        else:
            id_dict[a[1]] = a[2]

    for i in range(len(answer)):
        a = answer[i].split('님')[0]
        answer[i] = answer[i].replace(a,id_dict[a])

    return answer