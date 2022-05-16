switch_count = int(input())
switch_onoff = list(map(int, input().split()))
students_count = int(input())
gender_switch_list = [list(map(int, input().split())) for _ in range(students_count)]

def change_switch(onoff):
    if onoff == 1:
        onoff -= 1
    else:
        onoff += 1
    return(onoff)

for i in gender_switch_list:
    if i[0] == 1:
        for j in range(i[1]-1,switch_count,i[1]):
            switch_onoff[j] = change_switch(switch_onoff[j])
    elif i[0] == 2:
        y = i[1] -1
        x = 1
        switch_onoff[y] = change_switch(switch_onoff[y])
        while 0 <= (y-x) < switch_count and 0 <= (y+x) < switch_count:
            if switch_onoff[y-x] == switch_onoff[y+x]:
                switch_onoff[y-x] = change_switch(switch_onoff[y-x])
                switch_onoff[y+x] = change_switch(switch_onoff[y+x])
                x += 1
            else:
                break

for i in range(len(switch_onoff)):
    print(switch_onoff[i], end=' ')
    if (i+1) % 20 == 0:
        print()
        