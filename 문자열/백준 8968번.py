T = int(input())

for i in range(T):
    N = input()
    M = list(map(str, N.split('X')))
    total = 0
    for j in M:
        total += len(j) * (len(j)+1) / 2
        
    print(int(total))
        
    