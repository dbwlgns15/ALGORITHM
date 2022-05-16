students = int(input())
num_list = list(map(int, input().split()))
students_list = []
for i in range(students):
    students_list.insert(num_list[i],i+1)
students_list.reverse()
for i in range(students):
    print(students_list[i],end=' ')