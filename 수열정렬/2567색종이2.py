def f(i, j):
  global ans
  cnt = 0
  for d in range(4):
    y = i +dy[d]
    x = j +dx[d]
    if 0<=y<102 and 0<=x<102 and visited[y][x] == 1:
      cnt += 1
  ans += cnt
  return

import sys
input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
n = int(input())
visited =[[0]*102 for _ in range(102)] 

for i in range(n):
  a, b = map(int, input().split())
  for i in range(a+1, a+11):
    for j in range(b+1, b+11):
      visited[i][j] = 1
# print(visited)
ans = 0
for i in range(102):
  for j in range(102):
    if visited[i][j] == 0:
      f(i, j)

print(ans)

  