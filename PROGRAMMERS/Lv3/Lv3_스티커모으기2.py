def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    if len(sticker) == 2:
        return max(sticker[0],sticker[1])
    sticker1 = sticker[:-1]
    sticker2 = sticker[1:]
    def check_dp(table):
        dp = [0]*len(table)
        dp2 = [0]*len(table)

        dp[0] = table[0]
        dp2[0] = 1

        dp[1] = max(table[0],table[1])
        if dp[1] == table[0]:
            dp2[1] = -1
        else:
            dp2[1] = 1

        for i in range(2,len(table)):
            if dp2[i-1] == -1:
                dp[i] = dp[i-1] + table[i]
            else:
                if dp[i-1] >= dp[i-2] + table[i]:
                    dp[i] = dp[i-1]
                    dp2[i] = -1
                else:
                    dp[i] = dp[i-2] + table[i]
                    dp2[i] = 1
        return dp[-1]
    answer = max(check_dp(sticker2),check_dp(sticker1))
    return answer