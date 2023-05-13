def bfs():
  while q: # 움직일 수 없을때까지 실행
    n = q.popleft()

    if n == k: # 목표좌표 도달하면 
      return vn[n] - 1 # 움직 -1 , +1 움직인 수 출력
    
    if 0<=n*2<mx and vn[n*2]==0: # 2배로 순간이동은  이동횟수로 생각 x 
      #  최대값보다 작고 방문한 적이 없으면
      vn[n*2] = vn[n] # 방문처리 >> 이동횟수로 생각 안하니 +0 
      q.append(n*2) # n*2 좌표를 q에 넣기
    if 0<=n-1 and vn[n-1]==0: # n-1 , n+1 움직인 횟수로 생각하니까 
        vn[n-1] = vn[n] + 1 # 방문처리할때 +1 해주기
        q.append(n-1)       # n-1 좌표 저장
    if 0<=n+1<mx and vn[n+1]==0:
        vn[n+1] = vn[n] + 1 
        q.append(n+1) # n+1 좌표저장


from collections import deque
n, k = map(int, input().split()) # 시작점 목표점
mx = 100001  # 최대 움직일 수 있는 거리 100000 : 리스트로 받아야 하니까 100001까지
vn = [0] * 100001 # 방문처리 할 리스트
vn[n] = 1 # 현재 위치 방문처리
q = deque() # 움직일 수 있는 좌표 받을 데큐
q.append(n) # 현재 위치 넣기
print(bfs())
