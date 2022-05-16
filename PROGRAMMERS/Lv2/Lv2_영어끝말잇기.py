words = ["hello", "one", "even", "never", "now", "world", "draw"]
n = 2

chk = 0
words_dict = {words[0]:1}
for i in range(1,len(words)):
    if words_dict.get(words[i]):
        chk = i+1
        break
    else:
        words_dict[words[i]] = 1
    if words[i-1][-1] != words[i][0]:
        chk = i+1
        break
if chk == 0 :
    answer = [0,0]
else:
    answer = [chk%n,chk/n]
    if answer[0] == 0:
        answer[0] = n
    if answer[1] != int(answer[1]):
        answer[1] = int(answer[1])+1

print(answer)





