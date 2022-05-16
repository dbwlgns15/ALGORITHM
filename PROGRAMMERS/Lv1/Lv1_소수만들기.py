import itertools

def solution(nums):

    comb_list = itertools.combinations(nums,3)

    cnt = 0
    for i in list(comb_list):
        n = sum(i)
        x = 1
        for j in range(2,int(n**(1/2))+1):
            if n % j == 0:
                x = 0
        cnt += x

    return cnt