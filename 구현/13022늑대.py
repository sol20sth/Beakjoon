word = input()
if len(word) == 0:
    print(0)
else:
    for i in range(1, len(word)//4+1):
        tmp = 'w'*i + 'o'*i + 'l'*i + 'f'*i
        
        while tmp in word:
            word = word.replace(tmp, '')
    print(word)
    if len(word) == 0:
        print(1)
    else:
        print(0)
