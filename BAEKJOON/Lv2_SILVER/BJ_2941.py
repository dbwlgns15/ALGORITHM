text = input()
c_word = ['c=','c-','d-','dz=','lj','nj','s=','z=']
for i in c_word:
    text = text.replace(i,' ')
print(len(text))