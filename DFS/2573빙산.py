from collections import deque
import sys
input = sys.stdin.readline

def TF(y, x):   # 해당 리시트범위 확인 함수
  if 0<=y<n and 0<=x<m:
    return True
  else:
    False
    
def melt():  # 4방향 탐색해서 빙산이 녹게 만들어 주는 함수
  global sea
  ice_count = 0  # 리스트내의 빙산의 개수 변수
  tmpsea = [[0] * m for  _ in range(n)]  # 바다 리스트를 만들기 위한 임시 리스트 >> 
  # 그냥 리스트를 빙산을 녹게 만들면서 탐색하면 도중에 0이되는 값이 생기기 때문에 
  for i in range(n):  # 전체 리스트 탐색
    for j in range(m):
      cnt = 0  # 주변의 바다 개수를 받을 변수
      for d in range(4):  # 현재 위치에서 4방향 탐색
        yy, xx = i + dy[d], j + dx[d]  
        if TF(yy, xx) and sea[yy][xx] == 0: # 리스트내에 존재하고 바다이면 +1
          cnt += 1
      if sea[i][j] - cnt > 0: # 빙산이 남아있다면
        tmpsea[i][j] = sea[i][j] - cnt # 빙산 임시리스트에 남아있는 수 넣어주기
        ice_count += 1  # 리스트내의 빙산개수 1개추가
      else:  # 빙산이 남아있지 않고 바다이면
        tmpsea[i][j] = 0  # 리스트내의 빙산개수를 0으로 설정 -값도 나올 수 있으니
  sea = tmpsea  # 바다를 최종적으로 구한 리스트로 변경
  return ice_count   # 빙산의 개수를 빼내기
      
def find_start():  # 바다리스트에서 빙산이있는 곳 아무곳이나 찾기 >> 시작점은 바다만 아니면 상관이 없다
  for i in range(n):
    for j in range(m):
      if sea[i][j] != 0:
        return i , j  # 좌표 리턴
  
def bfs(find, ans):  # bfs 탐색 (빙산의 개수, 흐른시간)
  if sea == [[0]*m for _ in range(n)]: # 만약에 다녹아버리고 없다면 0을 프린트 후 함수 종료
    print(0)
    return
  y, x = find_start()  # 탐색 시작할 좌표 설정
  cnt = 1  # 현재 위치에서 붙어있는 빙산의 개수 받을 변수
  visited = [[0]*m for _ in range(n)]  # 방문 확인 리스트
  visited[y][x] = 1  # 현재 위치 방문처리
  q = deque()  # 붙어있는 빙산의 좌표 받을 deque
  q.append((y, x))  # 현재 위치 빙산에 추가
  while q: # 탐색할 위치 없을때까지 
    y, x = q.popleft()  # 현재위치 설정
    for d in range(4): # 4방향 탐색
      yy, xx = y+dy[d], x + dx[d] 
      if TF(yy, xx) and visited[yy][xx] == 0 and sea[yy][xx] !=0:
        # 좌표가 리스트내에 존재하고 방문한적없고 빙산이라면 
        visited[yy][xx] = 1  # 방문처리
        q.append((yy, xx)) # 빙산좌표에 추가
        cnt += 1  # 빙산 개수 추가
  # print(sea, visited, find)
  if cnt != find:  # 붙어있는 빙산의 개수와 총 빙산의 개수가 다르다면 나누어졌다고 생각되기때문에
    print(ans)  # 흐른시간을 프린트후 함수종료
    return
  else:  # 만약 같다면 
    bfs(melt(), ans+1) # 녹는 함수 한번실행후 재탐색 >> 시간이 +1 만큼 흐르게 하고
    

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)] # 빙산의 리스트
bfs(melt(), 1)













