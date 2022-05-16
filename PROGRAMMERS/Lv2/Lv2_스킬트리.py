import re
def solution(skill, skill_trees):
    a = f'[{skill}]'
    answer = 0
    for i in skill_trees:
        try:
            chk = ''.join(re.findall(a,i))
            if skill[:len(chk)] == chk:
                answer += 1
        except:
            answer += 1

    return answer