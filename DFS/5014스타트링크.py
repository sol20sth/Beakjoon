from collections import deque

def bfs(s):
  visited = [0] * (f+1) # 빌딩 높이 마다 방문처리
  visited[s] = 1 # 현재 위치 방문처리
  q = deque() # 빈데큐
  q.append(s) # 현재 위치 넣기
  while q: # q가 빌떄까지 반복
    s = q.popleft() # q의 0번인덱스 뽑아내 현재위치로 설정
    if s == g: # 만약 목표위치 도착하면
      return visited[g]-1 # 방문값 -1 >> 처음위치부터 1로 잡았으니
    for i in (s+u, s-d): # 현재위치에서 내려간곳 올라간곳 탐색
      if 0<i<=f and not visited[i]: # 빌딩 높이가 옳고 방문한 적이 없는 높이면
        visited[i] = visited[s] + 1 # 방문 순서 +1 넣기
        q.append(i) # 위치 넣기
  if visited[g] == 0: # 만약 목표 층을 방문한 적이 없으면
    return 'use the stairs' # 계단으로 가라

f, s, g, u, d = map(int, input().split()) # 최대 높이, 시작, 목표, 위, 아래
cnt = 0
print(bfs(s))