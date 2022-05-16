n = int(input())
n_list = list(map(int,input().split()))
if n == 1 or n == 2:
    print(0)
else:
    n_dict = {}
    m_list = []
    m_list.append(n_list.pop())
    for _ in range(len(n_list)):
        x = n_list.pop()
        for y in m_list:
            n_dict[x+y] = 1
        m_list.append(x)
    answer = 0
    for i in m_list:
        answer += n_dict.get(i,0)
    print(answer)