paper_count = int(input())
point_list = [list(map(int, input().split())) for i in range(paper_count)]
full_paper = []
[full_paper.append([i,j]) for k in range(paper_count) for i in range(point_list[k][0],point_list[k][0]+10) for j in range(point_list[k][1],point_list[k][1]+10) if [i,j] not in full_paper]
print(len(full_paper))