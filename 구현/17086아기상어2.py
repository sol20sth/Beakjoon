n, m  = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]
stack = []
for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            stack.append((i, j))
mmx = 0

for i in range(n):
    for j in range(m):
        if li[i][j] == 0:
            mx = 2501
            for a, b in stack:
                tmp1 = abs(a-i)
                tmp2 = abs(b-j)
                
                mx = min(mx, max(tmp1, tmp2))
        mmx = max(mx, mmx)
print(mmx)