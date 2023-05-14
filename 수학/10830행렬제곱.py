n, b = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

def f(li, li2):
    li2 = [[0] * n for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                li2[i][j] += li[i][k] * li[k][j] % 1000
    return li2

def g(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                li[i][j] %= 1000
        return li
    tmp = g(a, b//2)
    if b % 2:
        return f(f(tmp, tmp), li)
    else:
        return f(tmp, tmp)

result = g(li, b)
for r in result:
    print(*r)