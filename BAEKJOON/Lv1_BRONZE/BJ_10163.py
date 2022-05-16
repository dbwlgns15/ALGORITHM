paper_count = int(input())

plane = [0]*1001*1001

for i in range(paper_count):
    x, y, a, b = map(int, input().split())
    for j in range(x,x+a):
        plane[j*1001+y:j*1001+y+b] = [i+1]*b

total_count = [0]*paper_count
for i in plane:
    if i != 0:
        total_count[i-1] += 1

for i in total_count:
    print(i)