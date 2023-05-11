# n*n 공간 
# 물고기 m
# 아기상어 1마리 크기 2


# 큰것 못지나감
# 같은 지나감
# 작은것 지나감 먹음

# ㄱ크기있고 자연수

def find_child():
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                return i, j
def TF(y, x):
    if 0<=y<n and 0<=x<n:
        return 1
    return 0

def bfs(y, x, size, cnt):
    global ans
    visited = [[0]* n for _ in range(n)]
    visited[y][x] = 1
    q = deque()
    q.append([y, x])
    print(sea, visited, y, x)
    while q:
        y, x = q.popleft()
        for d in range(4):
            yy, xx = y + dy[d], x + dx[d]
            if TF(yy, xx):
                if sea[y][x] >= sea[yy][xx] and visited[yy][xx]==0:
                    q.append([yy, xx])
                    visited[yy][xx] = visited[y][x] + 1
                    if sea[yy][xx] != 0:
                        sea[y][x] = 0
                        cnt += 1
                        if cnt == size:
                            sea[yy][xx] = 0
                            ans += visited[yy][xx] +1
                            bfs(yy, xx, size+1, 0)
                            
                        else:
                            sea[yy][xx] = 0
                            ans += visited[yy][xx] +1
                            bfs(yy, xx, size, cnt)
                
from collections import deque

dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]
n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]

[y, x] = find_child()
sea[y][x] = 2
ans = 0

bfs(y, x, 2, 0)
print(ans)


