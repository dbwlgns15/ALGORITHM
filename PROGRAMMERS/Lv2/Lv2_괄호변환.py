def solution(p):
    def check_bal(txt):
        cnt = 0
        for i in txt:
            if i == '(':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    txt = txt[1:-1]
                    txt2 = ''
                    for j in txt:
                        if j == '(':
                            txt2 += ')'
                        else:
                            txt2 += '('
                    return txt2
        return txt
        
    def spliting(txt):
        if txt == '':
            return ''
        cnt = 0
        for i in range(len(txt)):
            if txt[i] == '(':
                cnt += 1
                if cnt == 0:
                    u = txt[:i+1]
                    v = txt[i+1:]
                    break
            else:
                cnt -= 1
                if cnt == 0:
                    u = txt[:i+1]
                    v = txt[i+1:]
                    break
        if u == check_bal(u):
            return u+spliting(v)
        else:
            return '('+spliting(v)+')'+check_bal(u)
    return spliting(p)