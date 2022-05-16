n = int(input())
ox_list = [input() for _ in range(n)]

for ox in ox_list:
    answer = 0
    cnt = 0
    for i in ox:
        if i == 'X':
            cnt = 0
        if i == 'O':
            cnt += 1
            answer += cnt
    print(answer)
