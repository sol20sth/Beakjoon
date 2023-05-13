import sys
input = sys.stdin.readline

dy, dx = [1, -1, 0, 0 ] , [0, 0 , 1, -1]
def dfs(y, x):
    if y==n-1 and x==m-1: # 끝에 도착하면 1 리턴
        return 1
    if visited[y][x] != -1: # 끝이 아니고 한번 방문한 값이면 현재자리에서는 마지막까지 갈 수 있는 개수를 저장한 값으로 사용
        return visited[y][x]
    visited[y][x] = 0 # 방문한 적없으면 0으로 설정 후 끝까지 탐색
    for d in range(4): 
        yy, xx = y + dy[d], x + dx[d] # 4방향 탐색
        if 0 <= yy < n and 0 <= xx < m: # 범위내에 있으면
            if board[yy][xx] < board[y][x]: # 이동 위치가 더 낮으면
                visited[y][x] += dfs(yy, xx) # 현재자리에서 목표까지 도착가능 횟수 = 이동가능 위치에서 이동가능 횟수들을 더해준다
    return visited[y][x] # 마지막까지 가면 0, 0에서 끝까지 갈 수 있는 모든 경우의 수를 찾을 수 있다.



n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)] # true , false로 안하는 이유는 방문한적x, 방문했지만 끝까지 못간다:0, 방문했는데 끝까지 간 값들:x 
# 이렇게 최소 3개의 값이 필요하기 떄문
print(dfs(0, 0))

