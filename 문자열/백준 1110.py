T = input()
if len(T) == 1:
    T = T + '0'
S = T

def cycle(T):
    total = 0
    new_number = 0
    for i in range(2):
        total += int(T[i])
    new_number = T[-1] + str(total)[-1]
    T = new_number
    return T

count = 1
while True:
    if cycle(T) == S:
        print(count)
        break
    else:
        T = cycle(T)
        count += 1