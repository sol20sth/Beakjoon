def bfs(time):
  while q: # 움직일 수 없을때까지 실행
    n = q.popleft()
    if 0<= n-1 and visited[n-1] == 0:
      visited[n-1] = visited[n] + 1
      q.append(n)

from collections import deque
n, m = map(int, input().split())
q = deque()
mx = 100001
visited = [0] * mx
q.append(n)
visited[q] = 1
bfs(0)