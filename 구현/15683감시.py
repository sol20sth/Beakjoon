import sys
input = sys.stdin.readline

view1 = [(0,1), (0, -1), (-1, 0), (1, 0)]
view2 = [((0, 1), (0, -1)), ((1, 0), (-1, 0))]
view3 = [((1, 0), (0, 1)), ((1, 0), (0, -1)), ((-1, 0), (0, 1)), ((-1, 0), (0, -1))]

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
stack = []
for i in range(n):
    for j in range(m):
        if li[i][j] == 0 or li[i][j] == 6:
            continue
        else:
            stack.append((i, j))

for i, j in stack:
    if li[i][j] == 5 :
        for d in view1:
            x = j 
            y = i
            while True:
                x += d[1]
                y += d[0]
                if y<0 or x<0 or y>=n or x>=m:
                    break
                elif li[y][x] == 6:
                    break
                elif li[y][x] == 0:
                    li[y][x] = 7
                    