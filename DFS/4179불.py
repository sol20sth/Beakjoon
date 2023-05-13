def start():  # 출발점과 불의 위치를 저장 하고 방문처리하기 위한 함수
  for i in range(n):
    for j in range(m):
      if maze[i][j] == 'J': # 출발위치이면
        qj.append((i,j)) # 출발위치에 데큐에 추가
        visited[i][j] = 1 # 방문처리
      if maze[i][j] == 'F': # 불이면 
        qf.append((i, j)) # 불위치 데큐에 추가
        v_fire[i][j] = 1 # 불 방문처리
  return 

def TF(y, x):  # 미로내에 있는지 확인 함수
  if 0<=y<n and 0<=x<m:
    return True
  return False

def bfs():
  while qf:  # 불이 있을때까지
    y, x = qf.popleft()  # 불위치 설정
    for d in range(4): # 4방향 탐색
      yy, xx = y + dy[d], x + dx[d]
      if TF(yy, xx) and maze[yy][xx]!='#' and v_fire[yy][xx]==0: # 미로내에 있고 '#'이 아니며 방문한적 없으면
        v_fire[yy][xx] = v_fire[y][x] + 1 # 불 방문처리 거리 1늘려서
        qf.append((yy, xx)) # 불위치 추가

  while qj:  # 본인이 이동할 수 있는 곳까지 이동
    y, x = qj.popleft() # 현재 위치 재설정
    for d in range(4): # 4방향 탐색
      yy, xx = y + dy[d], x + dx[d]
      if TF(yy, xx): # 미로내에 있으면
        if visited[yy][xx] == 0 and (visited[y][x]+1 < v_fire[yy][xx] or not v_fire[yy][xx]) and maze[yy][xx] != '#':
          # 방문한적 없고 불이 방문한적 없거나 불의 거리보다 본인의 위치에서 거리가 작고 #이 아니면
          visited[yy][xx] = visited[y][x] + 1 # 방문처리 
          qj.append((yy, xx)) # 현재위치 추가
      else: # 미로밖에 있으면 >> 탈출 성공
        return visited[y][x]
  return 'IMPOSSIBLE' # 다돌았는데  탈출 못했으면 불가능 
        
  
from collections import deque


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)] # 미로리스트
v_fire = [[0]*m for _ in range(n)] # 불 방문처리
visited = [[0]*m for _ in range(n)] # 본인 방문처리
qj, qf = deque(), deque() # 본인과 , 불 위치 받을 데큐
start() 

print(bfs())
