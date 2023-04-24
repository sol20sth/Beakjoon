

def f(y, x , cnt, remain, visited):
  global mx
  mx = max(cnt, mx)  # 최대값 재설정
  q = []   
  q.append([y, x])
  while q:   # 탐색할 곳이 있을때까지 탐색
    # print(q, cnt, remain)
    y, x = q.pop()  # 현재 위치 재설정
    for d in range(4):  # 4방향 탐색
      yy, xx = y + dy[d], x + dx[d]  # 이동 할 위치 설정
      if 0<=yy<n and 0<=xx<n and visited[yy][xx] == 0 and arr[yy][xx]<arr[y][x]:  # 좌표평면에 존재, 방문한적 없고, 현재 위치가 방문할 위치보다 높으면
        visited[yy][xx] = 1 # 방문할 위치 방문처러
        f(yy, xx, cnt+1, remain, visited)  # 방문 >> 등산로개수 +1
        visited[yy][xx] = 0 # 방문 취소 후 재 탐색
      elif 0<=yy<n and 0<=xx<n and remain==1 and visited[yy][xx] == 0 and arr[y][x]>arr[yy][xx]-k:  # 방문한 적 없고 
                                # 현재 위치의 높이가 방문할 위치의 높이에서 최대로 깍을 수 있는 높이 를 빤 것보다 높으면
        visited[yy][xx] = 1  # 방문처리 
        tmp = arr[yy][xx]   # 방문할 위치 높이 저장
        arr[yy][xx] = arr[y][x] -1   # 방문 할 위치의 높이를 현재 높이에서 -1높이로 깍기
        f(yy, xx, cnt+1, 0, visited)  # 남은 횟수 줄이고 방문위치로 이동
        visited[yy][xx] = 0  # 방문 취소 처리
        arr[yy][xx] = tmp  # 원래 높이로 다시 만들기


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]  # 4방향 탐색
T = int(input())
for tc in range(1, T+1): 
  n, k = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(n)]
  top = []  # 최대 봉우리 좌표 리스트
  mx_top = 0 # 봉우리 최대 높이 
  for i in range(n):  # 전체 탐색
    for j in range(n):
      if arr[i][j] > mx_top:  # 현재 위치가 최대 높이 보다 크면
        top = []   # 최대 높이 리스트 초기화
        mx_top = arr[i][j]  # 최대 높이 재설정
        top.append([i, j])  # 최대 높이 좌표 리스트 추가
      elif arr[i][j] == mx_top:  # 같다면
        top.append([i, j]) # 최대 높이 좌표 리스트에 추가
  # print(top)
  mx = 0   # 최대 등산로 개수 변수
  for i, j in top:  # 최대 등산로 좌표들로 탐색
    visited = [[0] * n for _ in range(n)] # 방문한지 안한지 받을 리스트
    visited[i][j] = 1  # 현재 위치 방문처리
    f(i, j, 1, 1, visited) # 좌표, 등산로 개수, 등산로 깍을 수 있는 횟수, 방문처리 리스트
  print(f'#{tc} {mx}')