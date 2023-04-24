T = int(input())
for i in range(T):
    word = list(input())
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+2:]:
            T -= 1
            break
print(T)
            