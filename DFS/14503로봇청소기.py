def dfs(y, x, d):
  cnt = 1 # 현재위치 +1
  visited = [[0]*m for _ in range(n)] # 방문확인 리스트
  visited[y][x] = 1 # 현재위치 방문표시
  
  while True:
    for _ in range(4):
      d = (d+3) % 4 # 반시계방향으로 탐색 위해 방향 전환
      yy, xx = y+dy[d] , x + dx[d] # 방향으로 한칸 앞 탐색
      if 0<=yy<n and 0<=xx<m and room[yy][xx]==0: # 청소 안되어있고 방안이면
        if visited[yy][xx] == 0: # 방문한 적 없으면
          visited[yy][xx] = 1 # 방문처리
          cnt += 1 # 횟수 +1
          y, x = yy, xx # 좌표이동
          break
    else: # 4방향 탐색 후 모두 해당 안되면
      if room[y-dy[d]][x-dx[d]] == 1: # 한칸 뒤가 벽이면 종료
        print(cnt)
        break
      else: # 한칸 뒤가 벽이 아니면
        y, x= y-dy[d], x-dx[d] # 방향그대로 좌표만 이동
    
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
n, m = map(int, input().split()) # 방 세로 가로 크기
y, x, d = map(int, input().split()) # 로봇청소기 좌표, 방향
room = [list(map(int, input().split())) for _ in range(n)]
dfs(y, x, d)
