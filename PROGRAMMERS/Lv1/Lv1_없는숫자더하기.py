def solution(numbers):
    answer = 45
    for i in list(set(numbers)):
        answer -= i
    return answer