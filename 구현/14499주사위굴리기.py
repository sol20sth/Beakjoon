
n, m, x, y, k = map(int, input().split())
mapAll = [list(map(int, input().split())) for _ in range(n)]
commend = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
dx , dy = [0, 0, -1, 1], [1, -1, 0, 0]


for i in commend:
    i = i-1
    xx, yy = x+ dx[i], y+dy[i]
    if xx<0 or xx>=n or yy<0 or yy>=m:
        continue
    else:
        if i == 0:
            dice[0], dice[2], dice[5], dice[3]= dice[3], dice[0],  dice[2], dice[5]
        elif i == 1:
            dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
        elif i == 2:
            dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[2]
        else: 
            dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]
        
        if mapAll[xx][yy] == 0:
            mapAll[xx][yy] = dice[5]
        else:
            dice[5] = mapAll[xx][yy]
            mapAll[xx][yy] = 0
        x, y = xx, yy
        print(dice[0])
