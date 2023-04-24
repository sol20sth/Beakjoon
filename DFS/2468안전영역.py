def bfs(i,j,k):   # 행 열 물의높이 bfs
  cnt = 1         # 구간에 들어있는 집개수
  q = []
  q.append((i,j))   
  visited[i][j] = 1   # 방문
  while q:    # 방문 할 곳 있을때
    y,x = q.pop(0)    # 빼서 현재위치로
    for d in range(4):    # 4방향 탐색
      yy = y + dy[d]
      xx = x + dx[d]
      if 0<=yy<n and 0<=xx<n and visited[yy][xx] ==0 and arr[yy][xx]>k:   # 높이가 k보다 크고 방문한적없고 구간내면
        q.append((yy,xx))   # 위치 추가
        visited[yy][xx] = 1   # 방문 표시
        cnt += 1    # 집 개수 추가
  return cnt  
import sys
input = sys.stdin.readline
dy = [-1,1,0,0]
dx = [0,0,-1,1]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mxh = 0
for i in range(n):
    for j in range(n):
        mxh = max(mxh, arr[i][j])   # 주어진 집 높이중 가장 높은 곳 찾기
ans = 0   # 답
for k in range(mxh+1):    # 최대 높이 까지 탐색
  visited = [[0]*n for _ in range(n)]   # 방문표시
  stack = []    # 구간들 모음
  for i in range(n):
    for j in range(n):
      if arr[i][j] > k and visited[i][j]==0:    # k보다 높고 방문한적 없으면
        stack.append(bfs(i,j,k))      # 구간의 집 개수 스택에 추가
  
  ans = max(ans, len(stack))    # 구간의 개수와 답 비교해서 큰값 재설정
        
print(ans)
