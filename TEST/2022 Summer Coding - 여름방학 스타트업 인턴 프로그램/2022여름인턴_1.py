def solution(atmos):
    mask = [0] * (len(atmos)+2)
    cnt = 0

    for i in range(len(atmos)):
        a = atmos[i][0]
        b = atmos[i][1]
        if a > 80 or b > 35:
            if a > 150 and b > 75:
                if mask[i] == 0:
                    cnt += 1
                    mask[i] = cnt
                else:
                    mask[i+1] = 0
            else:
                if mask[i] == 0:
                    cnt += 1
                    mask[i] = cnt
                    mask[i+1] = cnt
                    mask[i+2] = cnt

    answer = cnt
    return answer