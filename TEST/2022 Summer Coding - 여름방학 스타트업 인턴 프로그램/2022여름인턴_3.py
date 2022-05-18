def solution(line):
    p_dict = {'1':[1,1],'2':[1,2],'3':[1,3],'4':[1,4],'5':[1,5]
    ,'6':[1,6],'7':[1,7],'8':[1,8],'9':[1,9],'0':[1,10],'Q':[2,1]
    ,'W':[2,2],'E':[2,3],'R':[2,4],'T':[2,5],'Y':[2,6],'U':[2,7]
    ,'I':[2,8],'O':[2,9],'P':[2,10]}
    result = []
    l,r = 'Q','P'
    for i in line:
        c_l = abs(p_dict[l][0] - p_dict[i][0]) + abs(p_dict[l][1] - p_dict[i][1])
        c_r = abs(p_dict[r][0] - p_dict[i][0]) + abs(p_dict[r][1] - p_dict[i][1]) 
        if c_l == c_r:
            cc_l = abs(p_dict[l][1] - p_dict[i][1])
            cc_r = abs(p_dict[r][1] - p_dict[i][1])
            if cc_l == cc_r:
                if i in ['1','2','3','4','5','Q','W','E','R','T']:
                    l = i
                    result.append(0)
                else:
                    r = i
                    result.append(1)
            else:
                if cc_l < cc_r:
                    l = i
                    result.append(0)
                else:
                    r = i
                    result.append(1)
        else:
            if c_l < c_r:
                l = i
                result.append(0)
            else:
                r = i
                result.append(1)

    return result