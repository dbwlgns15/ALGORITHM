def solution(numbers, hand):
    xy = {'1':[1,4], '2':[2,4], '3':[3,4], '4':[1,3], '5':[2,3], '6':[3,3],
          '7':[1,2], '8':[2,2], '9':[3,2], '*':[1,1], '0':[2,1], '#':[3,1]}

    l = '*'
    r = '#' 
    answer = ''
    for i in numbers:
        i = str(i)
        if i in ['1','4','7']:
            l = i
            answer += 'L'
        elif i in ['3','6','9']:
            r = i
            answer += 'R'
        else:
            n_xy = xy[i]
            l_xy = xy[l]
            r_xy = xy[r]
            n_l = abs(n_xy[0]-l_xy[0]) + abs(n_xy[1]-l_xy[1])
            n_r = abs(n_xy[0]-r_xy[0]) + abs(n_xy[1]-r_xy[1])
            if n_l < n_r:
                l = i
                answer += 'L'
            elif n_l > n_r:
                r = i
                answer += 'R'
            else:
                if hand == 'left':
                    l = i
                    answer += 'L'
                else:
                    r = i
                    answer += 'R'

    return answer