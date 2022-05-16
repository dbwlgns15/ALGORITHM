n = int(input())
n_list = [int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = n_list[0]
if n >= 2:
    dp[1] = n_list[0]+n_list[1]
if n >= 3:
    dp[2] = max(n_list[1]+n_list[2],  n_list[0]+n_list[2])
    for i in range(3,n):
        dp[i] = max(dp[i-2]+n_list[i],  dp[i-3]+n_list[i]+n_list[i-1])
    
print(dp[n-1])
