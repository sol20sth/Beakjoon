def check(remain):
  global mi, sm
  if remain == 3:
    mi = min(mi, sm)
    return
  # print(remain, sm)
  for i in range(1, n-1):
    for j in range(1, n-1):
      can_place = True
      for d in range(5):
        yy , xx = i + dy[d] , j + dx[d]
        if board[yy][xx] == 1:
          can_place = False
          break
      if can_place:
        for d in range(5):
          yy, xx = i +dy[d], j + dx[d]
          board[yy][xx] = 1
          sm += arr[yy][xx]
        check(remain+1)
        for d in range(5):
          yy, xx = i +dy[d], j + dx[d]
          board[yy][xx] = 0
          sm -= arr[yy][xx]
  
  
  
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dy = [0, -1, 0, 1, 0]
dx = [-1, 0, 0, 0, 1]
mi = 200001
sm = 0
board = [[0] * n for _ in range(n)]
check(0)
print(mi)
