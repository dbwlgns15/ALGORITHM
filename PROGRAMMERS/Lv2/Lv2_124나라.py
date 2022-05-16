def solution(n):
    n -= 1
    dict124 = {0:'1',1:'2',2:'4'}
    answer = ''
    while n > -1:
        a = n // 3
        b = n % 3
        answer = dict124[b] + answer 
        n = a - 1

    return answer