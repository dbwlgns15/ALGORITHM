test_time = int(input())
for i in range(test_time):
    p_word = 0
    word_count = int(input())
    word_list = [input() for i in range(word_count)]

    for i in range(len(word_list)):
        for j in range(i+1,len(word_list)):
            password1 = word_list[i] + word_list[j]
            password2 = word_list[j] + word_list[i]
            if password1 == password1[::-1]:
                p_word = password1
            if password2 == password2[::-1]:
                p_word = password2
    print(p_word)