from collections import deque
def TF(y, x):  # 범위내에 있느지 확인하는 함수
  if 0<=y<n and 0<=x<m:
    return True # 범위내에 있으면 참 리턴
  return False # 범위 밖에 있으면 거짓 리턴


def bfs(i, j): 
  global mx # 거리 뽑아낼 함수 
  q = deque() 
  q.append((i, j)) # 현재 위치 넣기
  visited =[[0] * m for _ in range(n)] # 방문 확인 할 리스트
  visited[i][j] = 1 # 현재위치 방문처리 
  while q: # q가 비어있을때까지 반복
    y, x = q.popleft() # 현재위치 재설정
    for d in range(4): # 4방향 탐색
      yy, xx = y + dy[d], x + dx[d]
      if TF(yy, xx) and visited[yy][xx]==0 and li[yy][xx] =='L':
        # 범위내에 있고, 방문한적 없으며, 육지이면
        q.append((yy, xx)) # 위치 저장
        visited[yy][xx] = visited[y][x] + 1 # 방문처리>> 거리 +1만큼
  mx = max(mx, visited[y][x]) # 반복문이 끝나면 가장 먼 거리의 좌표가 y, x 이므로
  # mx 값 재설정
  # print(mx)
    
dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
n, m = map(int, input().split())
li = [list(input()) for _ in range(n)]
mx = 0
for i in range(n):  # li 전체 탐색
  for j in range(m):
    if li[i][j] == 'L': # 육지이면

        bfs(i, j) # bfs 함수 실행
print(mx-1)