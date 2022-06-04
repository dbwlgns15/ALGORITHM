def solution(numbers):
    numbers.sort()
    answer = set()
    for i in range(len(numbers)): 
        for j in range(i+1,len(numbers)):
            a = numbers[i] + numbers[j]
            answer.add(a)
    return sorted(list(answer))