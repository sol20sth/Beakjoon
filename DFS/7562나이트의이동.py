'''
T 테스트케이스개수
n 체스판개수
now 현재위치
target 목표위치
'''
def bfs(y,x):
  q = []
  q.append((y,x))
  visited = [[0]*n for _ in range(n)]
  visited[y][x] = 1
  while q:
    y, x = q.pop(0)
    for d in range(8):
      yy , xx = y + dy[d], x + dx[d]
      if 0<=yy<n and 0<=xx<n and visited[yy][xx]



import sys
input = sys.stdin.readline
dy = [1, 2, 2, 1, -1, -2, -2, -1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
T = int(input())
for tc in range(T):
  n = int(input())
  y, x = map(int, input().split())
  ty, tx = map(int, input().split())
