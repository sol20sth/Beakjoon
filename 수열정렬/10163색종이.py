import sys
input = sys.stdin.readline

n = int(input())
visited = [[0]*1001 for _ in range(1001)]
num = 1
mxx ,mxy = 0, 0
for i in range(n):
  x, y, a, b = map(int, input().split())
  if mxx < x+a-1:
    mxx = x+a-1
  if mxy < y+b-1:
    mxy = y+b-1
  for i in range(x, x+a):
    for j in range(y, y+b):
      visited[i][j] = num
  num += 1
for i in range(1, n+1):
  cnt = 0
  for j in range(mxy):
    for k in range(mxx):
      if visited[j][k] == i:
        cnt += 1
  print(cnt)