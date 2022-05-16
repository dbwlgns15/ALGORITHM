def solution(money):
    def check_dp(money):
        dp = [0] * len(money)
        dp[0] = money[0]
        dp[1] = max(money[0],money[1])
        for i in range(2,len(money)):
            dp[i] = max(dp[i-1], dp[i-2]+money[i])
        return dp[-1]
    answer = max(check_dp(money[1:]),check_dp(money[:-1]))
    return answer