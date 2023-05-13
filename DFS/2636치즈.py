from collections import deque

def TF(y, x): # 범위내에 있는지 확인하는 함수
  if 0<=y<n and 0<=x<m:
    return True
  else:
    return False

def air(y, x,tmp): # 공기의 위치 저장하기 위한 함수
  q = deque() 
  q.append((y, x)) # 현재 위치 q에 추가
  visited = [[0] * m for _ in range(n)] # 방문한 곳인지 확인 할 리스트
  visited[y][x] = 1 # 현재 위치 방문처리
  while q: # q 가 비어있을 떄까지
    y, x = q.popleft() # q에서 뺴낸 위치로 이동
    for d in range(4): # 4방향 탐색
      yy, xx = y + dy[d], x + dx[d] 
      if TF(yy, xx) and visited[yy][xx] == 0 and tmp[yy][xx]==0:
        # 범위내에 존재하며, 방문한적 없고, 공기일때
        q.append((yy, xx)) # 방문하기 위해 저장
        visited[yy][xx] = 1 # 방문처리
  return visited # 방문한 리스트 뺴내기

def f(cheeze):
  global ans # 최종 시간

  while True: 
    tmp = [[0] * m for _ in range(n)] # 전체 치즈 리스트를 다시 받기 위한 임시 리스트
    for i in range(n): # 전체 탐색
      for j in range(m):
        tmp[i][j] = cheeze[i][j] # 임시리스트에 치즈리스트 넣어주기
    visited = air(0, 0, tmp) # 공기 리스트 뺴내기
    ans += 1 # 시간 +1
    cnt = 0 # 치즈 개수 샐 변수
    for i in range(1, n-1):  # 완전탐색 
      for j in range(1, m-1):
        if cheeze[i][j] == 1: # 치즈이면
          cnt += 1  # 치즈개수 +1
          for d in range(4): # 4방향 탐색
            yy, xx = i + dy[d], j + dx[d]
            if TF(yy, xx) : # 리스트 내에 존재하면
              if visited[yy][xx] == 1: # 공기이면
                tmp[i][j] = 0 # 치즈 없애기
                break # 끝내기
    cheeze = tmp # 치즈 다없애면 치즈리스트에 임시치즈리스트 넣기
    if tmp == [[0]*m for _ in range(n)]: # 만약 임시치즈리스트가 빈리스트면
      print(f'{ans}\n{cnt}') # 출력
      return 
    
        
            
dy, dx = [-1, 1, 0, 0] , [0, 0, 1, -1]
n, m = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(n)]
ans = 0
f(cheeze)

