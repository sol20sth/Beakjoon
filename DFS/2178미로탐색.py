def bfs(y, x, maze):
    q = []      # 빈 큐
    q.append((y,x)) # 현재 자리 추가
    maze[y][x] = 0  # 현재자리 방 문
    while q:
        y, x = q.pop(0) # 큐에서 뺀 값 현재위치로
        if (y, x) == (n, m):      # n,m 에 방문하면 
            return maze[y][x]+1 # 값을 빼낸다
        else:
            for d in range(4):  # 4방향 탐색
                yy = y + dy[d]
                xx = x + dx[d]
                if 0<=xx<m+1 and 0<=yy<n+1 and maze[yy][xx] == 1:   # 범위안이고 값이 1이면
                    q.append((yy,xx))   # 스택에 추가
                    maze[yy][xx] = maze[y][x] + 1   # 깊이 추가
    return



dy = [-1, 1, 0, 0]  # 움직일 방향
dx = [0, 0, -1, 1]         
n, m = map(int, input().split())
# 1, 1 시작인데 리스트에서 표현하기 위해 빈 0들 추가
maze = [[0]*(m+1)]+[[0]+[int(x) for x in input()] for _ in range(n)] 
print(bfs(1,1,maze)) # 시작점 1, 1 