def solution(n, text, second):
    answer = ['_']*n
    second = second%(n+len(text))
    text = text.replace(' ','_')
    text = text+'_'*n
    text = list(text)
    for _ in range(second):
        answer.pop(0)
        answer.append(text.pop(0))
    answer = ''.join(answer)
    return answer 