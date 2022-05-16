test_time = int(input())

for i in range(test_time):
    num, word = input().split()
    num = int(num)
    print(word[:num-1]+word[num:]) 