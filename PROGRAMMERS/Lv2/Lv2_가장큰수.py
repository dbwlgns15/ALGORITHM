def solution(numbers):
    answer = ''
    sum_ = 0
    tmp = []
    for number in numbers:
        c = (str(number) * 4)[:4]
        length = len(str(number))
        tmp.append((c, length))
    tmp.sort(reverse=True)
    for (c, length) in tmp:
        sum_ += int(c)
        if sum_ == 0:
            return '0'
        answer += c[:length]
    return answer