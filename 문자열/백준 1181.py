T = int(input())
word_list = []
for i in range(T):
    a = input()
    word_list.append(a)
    
word_set = list(set(word_list))
word_set.sort()
word_set.sort(key=len)

for i in word_set:
    print(i)
