import re
def solution(new_id):
    i = new_id.lower()
    i = re.sub('[^0-9a-z-_.]','',i)
    i = re.sub('\.+','.',i)
    i = i.strip('.')
    if len(i) > 15:
        i = i[:15]
    i = i.strip('.')
    if i == '':
        i = 'a'
    if len(i) < 3:
        i = i.ljust(3,i[-1])

    answer = i
    return answer