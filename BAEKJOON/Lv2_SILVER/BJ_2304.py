n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()
x = [i[0] for i in a]
y = [i[1] for i in a]
max_y_index = y.index(max(y))
ans = y[max_y_index]
while max_y_index > 0 :
    y_index = y[:max_y_index].index(max(y[:max_y_index]))
    ans += (x[max_y_index] - x[y_index]) * y[y_index]
    max_y_index = y_index
max_y_index = y.index(max(y))
while max_y_index < n-1 :
    y_index = max_y_index + y[max_y_index+1:].index(max(y[max_y_index+1:])) + 1
    ans += (x[y_index] - x[max_y_index]) * y[y_index]
    max_y_index = y_index
print(ans)