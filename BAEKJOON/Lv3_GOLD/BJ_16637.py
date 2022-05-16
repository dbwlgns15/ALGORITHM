import re

input()
text = input()
n = re.findall('[0-9]',text)
c = re.findall('[\+\-\*]',text)

def sol(n,c):
    if len(n) == 1:
        return n[0]
    dp = [0] * len(n)
    dp[0] = eval(n[0])
    dp[1] = eval(n[0]+c[0]+n[1])
    for i in range(2,len(n)):
        dp[i] = max(
            eval(str(dp[i-2])+c[i-2]+str(eval(n[i-1]+c[i-1]+n[i]))),
            eval(str(dp[i-1])+c[i-1]+n[i]))
    return(dp[-1])

print(sol(n,c))