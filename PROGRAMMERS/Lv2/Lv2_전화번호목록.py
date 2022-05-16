def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    chk = {}
    for i in phone_book:
        for j in range(len(i)):
            if chk.get(i[:j+1]):
                return False
        chk[i] = 1
    return answer