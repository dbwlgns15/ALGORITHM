def solution(board, moves):
    new_board = list(map(list, zip(*board)))
    new_board = [i[::-1] for i in new_board]

    doll_list = []
    answer = 0
    for i in moves:
        try:
            doll = 0
            while doll == 0:
                doll = new_board[i-1].pop()
            if len(doll_list):
                if doll_list[-1] == doll:
                    doll_list.pop()
                    answer += 2
                else:
                    doll_list.append(doll)
            else:
                doll_list.append(doll)
        except:
            pass
        
    return answer