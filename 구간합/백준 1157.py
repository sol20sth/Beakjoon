T = input().upper()
count = {}

for i in range(len(T)):
    if T[i] in count.keys():
        count[T[i]] += 1
    else:
        count[T[i]] = 1
max_key = max(count, key = count.get)
if len(list(count.keys())) != len(set(count.keys())):
    print('?')

else:

    print(max_key)


