# def bfs(y, x):
#   global cnt
#   visited = [[0] * m for _ in range(n)]
#   visited[y][x] = 1
#   q = deque()
#   q.append((y, x))
#   while q:
#     y, x = q.popleft()
#     if visited[y][x] == k:
#       return
#     for d in range(4):
#       yy , xx = y + dy[d], x + dx[d]
#       if 0<=yy<n and 0<=xx<m and visited[yy][xx] == 0 and arr[yy][xx]!='T':
#         if yy == 0  and xx == m-1 and visited[y][x]!=k-1:
#           break
#         elif yy == 0  and xx == m-1 and visited[y][x]==k-1:
#           cnt += 1
#           break
#         else:
#           visited[yy][xx] = visited[y][x] + 1
#           q.append((yy, xx))
# dy =[-1, 1, 0, 0]
# dx = [0, 0, 1, -1]



# import sys

# input = sys.stdin.readline
# n, m , k = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
# cnt = 0

# arr0 = [[1]+ [0] * (m-1) for _ in range(n-1)] + [[1] * m]

# for i in range(n-2, -1, -1):
#   for j in range(1, m):
#     if arr[i][j] == 'T': 
#       arr0[i][j] = 0
#     else:
#       arr0[i][j] = arr0[i-1][j] + arr0[i][j-1]
# ans = arr0[0][m-1]
# K = k//2 
# if k == n+m-1:
#   print(ans)
# else:
#   for i in range(n):
#     for j in range(m):
#       if abs(i-j) == m-1-K:
#         ans -= arr0[i][j]
#   print(ans)
  
################
n, m, K = map(int, input().split())
graph = [list(input()) for _ in range(n)]
answer = 0

def back(x, y, k):
    global answer
    if k == K:
        if (x, y) == (0, m - 1): 
            answer += 1
    else:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'T':
                graph[nx][ny] = 'T'
                back(nx, ny, k + 1)
                graph[nx][ny] = '.'

graph[n - 1][0] = 'T'
back(n - 1, 0, 1)
print(answer)