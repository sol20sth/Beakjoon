import sys
from collections import deque
input = sys.stdin.readline

def bfs(q, li): # bfs탐색
  global cnt, n, m, h
  visited = [[[0]*m for _ in range(n)] for _ in range(h)] # 방문처리할 3차원 리스트
  for i, j, k in q:  # q에 들어있는 좌표들을 모두 방문처리
    visited[i][j][k] = 1
  while q: # q가 비어있을때까지 탐색
    z, y, x = q.popleft()  # q[0]에서 뺴낸값을 현재 위치로 선택
    for d in range(6):  # 6방향 탐색
      zz, yy, xx = z + dz[d],y+ dy[d],x+ dx[d] # 현재위치에서 1칸씩이동한 좌표
      if 0<=yy<n and 0<=xx<m and 0<=zz<h and visited[zz][yy][xx] == 0 and li[zz][yy][xx] == 0: 
        # 리스트내에 존재하며 방문한적없으며 익지않은 토마토라면
        q.append([zz, yy, xx])  # q에 좌표추가
        visited[zz][yy][xx] = 1 + visited[z][y][x] #방문처리 >> 현재 토마토의 시간의 +1로 저장
        li[zz][yy][xx] = 1 # 익은 토마토로 만들기
        cnt += 1  # 익은 토마토 숫자
  return visited[z][y][x]-1  # 마지막으로 익은 토마토의 시간 리턴

m, n , h = map(int, input().split()) # x, y, z좌표
dx  = [-1, 1, 0, 0, 0, 0]  # 6방향 설정
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
li = [[list(map(int, input().split()))for _ in range(n)] for _ in range(h)] # 토마토 위치리스트
q,cnt = deque(), 0 # 익은 토마토 좌표받을 deque, 익은 토마토+아무것도 없는 좌표 개수 저장 변수
for i in range(h):
  for j in range(n):
    for k in range(m):
      if li[i][j][k] == 1: # 익은 토마토이면 q에 좌표넣기, 개수추가
        q.append([i, j, k])
        cnt += 1
      if li[i][j][k] == -1: # 아무것도 없으면 개수추가
        cnt += 1
if q: # return 시에 visited[z][y][x]를 하는데 q가 비어있으면 에러가 떠서 q가 있을때만 함수돌리기
  ans = bfs(q, li)
  if cnt != n*m*h: # 빈공간과 익은토마토의 개수가 전체가 아니면 -1출력
    print(-1)
  else:  # 모든 토마토가 익으면 bfs결과 출력
    print(ans)
else: # q가 비어있으면
  if cnt == n*m*h:  # 덜익은 토마토가 없으면 0출력
    print(0)
  else: #덜익은 토마토가 있으면 -1출력
    print(-1)
  