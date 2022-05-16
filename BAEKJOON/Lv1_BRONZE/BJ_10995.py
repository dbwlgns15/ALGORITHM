test_time = int(input())

for i in range(1,test_time+1):
    if i%2==1:
        print('* '*(test_time))
    else:
        print(' *'*(test_time))