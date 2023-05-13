import sys
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
m, n = map(int, input().split())
target = int(input())

arr = [[0]*m for _ in range(n)]
y, x, num, d = 0, 0, 2, 0
arr[0][0] = 1
if target > m * n:
  print(0)
else:
  while num != target+1:
    yy = y + dy[d]
    xx = x + dx[d]
    if 0<=yy<n and 0<=xx<m and arr[yy][xx]==0:
      arr[yy][xx] = num
      num += 1
      y ,x =yy, xx
      continue
    else:
      d = (d+1) % 4
      y, x = y + dy[d], x + dx[d]
      arr[y][x] = num
      num += 1    
  print(x+1, y+1)
  