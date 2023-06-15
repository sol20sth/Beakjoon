import sys

input = sys.stdin.readline
dy, dx = [0, -1, 0, 1], [1, 0, -1,0]

y, x, t = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(y)]

for _ in range(t):
    li2 = [[0] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            if li[i][j] == 0:
                continue
            elif li[i][j] != 0 and li[i][j] != -1:
                tmp = 0
                for d in range(4):
                    yy, xx = i + dy[d], j + dx[d]
                    if 0<=yy<y and 0<=xx<x and li[yy][xx] != -1:
                        li2[yy][xx] += li[i][j] // 5
                        tmp += 1
                li2[i][j] += li[i][j] - (li[i][j]//5 * tmp)
            else:
                li2[i][j] = -1

    first = True
    for i in range(y):
        for j in range(x): 
            if li2[i][j] != -1:
                continue
            yt, xt = i, j
            tmp, tmp2 = 0, 0
            if first == True:
                first = False
                while not(yt==i and xt==j and tmp == 3):
                    tmp3 = 0
                    yy, xx = yt + dy[tmp], xt + dx[tmp]
                    if 0<=yy<y and 0<=xx<x:
                        tmp3 = li2[yy][xx]
                        li2[yy][xx] = tmp2
                        tmp2 = tmp3
                        yt, xt = yy, xx
                    else: 
                        tmp += 1
                li2[i][j] = -1

            elif first == False:
                while not(yt==i and xt==j and tmp == 3):
                    tmp3 = 0
                    yy, xx = yt - dy[tmp], xt + dx[tmp]
                    if 0<=yy<y and 0<=xx<x:
                        tmp3 = li2[yy][xx]
                        li2[yy][xx] = tmp2
                        tmp2 = tmp3
                        yt, xt = yy, xx
                    else: 
                        tmp += 1
                li2[i][j] = -1
    li = li2
sm = 0
for i in range(y):
    sm += sum(li[i])
print(sm+2)