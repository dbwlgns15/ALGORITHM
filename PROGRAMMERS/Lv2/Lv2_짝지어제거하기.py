def solution(s):
    chk = []
    for i in s:
        if len(chk):
            j = chk.pop()
            if i != j:
                chk += [j,i]
        else:
            chk += [i]

    if len(chk):
        return 0
    else:
        return 1