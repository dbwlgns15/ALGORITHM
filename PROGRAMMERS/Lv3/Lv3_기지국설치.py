def solution(n, stations, w):
    check_list = [0]
    a = stations.pop()
    check_list[0] = n - a - w
    if check_list[-1] < 0:
        check_list[-1] = 0
    # print(check_list)
    while stations:
        b = stations.pop()
        # print('a',a,'b',b)
        check_list.append(a - b - 2*w -1)
        if check_list[-1] < 0:
            check_list[-1] = 0
        # print(check_list)
        a = b
    check_list.append(a - w - 1)
    # print(check_list)
    answer = 0
    for i in check_list:
        if i % (2*w+1) == 0:
            answer += i // (2*w+1)
        else:
            answer += i // (2*w+1)
            answer += 1
    # print(answer)

    return answer

solution(16,[9],2)