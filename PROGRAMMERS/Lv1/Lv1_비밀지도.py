def solution(n, arr1, arr2):
    for i in range(n):
        arr1[i] = format(arr1[i],'b').rjust(n,'0')
        arr2[i] = format(arr2[i],'b').rjust(n,'0')

    answer = [[' ']*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                answer[i][j] = '#'

    answer = [''.join(i) for i in answer]
    return answer