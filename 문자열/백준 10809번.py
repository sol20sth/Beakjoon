T = input()
box = [0]*26
alpa = 'abcdefghijklmnopqrstuvwxyz'

for i in T:
    for i in alpa:
        if i in T:
            box[ord(i) - 97] = T.index(i)
        else:
            box[ord(i) - 97] = -1
    

print(str(box)[1:-1].replace(',' ,""))
