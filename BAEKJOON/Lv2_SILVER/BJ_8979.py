n, k = map(int, input().split())
medal_list = [list(map(int, input().split())) for _ in range(n)]
medal_list.sort()
medal_list = list(map(list, zip(*medal_list)))
del medal_list[0]
medal_list = list(map(list, zip(*medal_list)))
chk = medal_list[k-1]
medal_list.sort(reverse=True)
ans = medal_list.index(chk) + 1
print(ans)