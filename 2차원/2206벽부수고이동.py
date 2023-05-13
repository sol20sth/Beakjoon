def dfs(y, x):
  global cnt, mi, tf
  visited = [[0]*m for _ in range(n)]
  visited[y][x] = 1
  stack = []
  while True:
    # print(y, x)
    if y==n-1 and x==m-1:
      mi = min(cnt, mi)
      tf = True
      return 
    if cnt > mi:
      return
    for d in range(4):
      yy , xx = y+dy[d] , x + dx[d]
      if 0<=yy<n and 0<=xx<m and visited[yy][xx]==0 and arr[yy][xx] == '0':
        stack.append([yy,xx])
        visited[yy][xx] = 1
        y , x = yy, xx
        cnt += 1
        break
    else:
      if stack:
        cnt -=1
        y, x = stack.pop()
      else:
        break
  return 
  
  
  
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
block = []
mi, tf= 1000000,False
for i in range(n):
  for j in range(m):
    cnt = 0
    if arr[i][j] == '1':
      arr[i][j] = '0'
      dfs(0, 0)
      arr[i][j] = '1'
if tf:
  print(mi-1)
else:
  print(-1)
