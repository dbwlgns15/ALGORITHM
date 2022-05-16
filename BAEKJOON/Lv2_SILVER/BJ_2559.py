days, t = map(int,input().split())
temp_list = list(map(int, input().split()))
max_temp = sum(temp_list[0:t])
next_temp = max_temp
for i in range(0,days-t):
    next_temp = next_temp + temp_list[i+t] - temp_list[i]
    if max_temp < next_temp:
        max_temp = next_temp
print(max_temp)