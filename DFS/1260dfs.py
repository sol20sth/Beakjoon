def dfs(x):
  visited[x] = 1
  print(x, end='')
  for i in range(n):
    if arr[v][i] == 1 and visited[v] == 0:
      dfs(i)

n, m, v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
  a, b = map(int, input().split())
  arr[a][b] = 1
  arr[b][a] = 1 
print(arr)

dfs(v)