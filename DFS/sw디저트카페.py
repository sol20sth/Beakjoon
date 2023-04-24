def f(y, x, cov, visited):
  global mx  
  if start[0] == y and start[1] == x and cov == 3: # 시작점에 왔는데 꺽은 횟수가 3이면 
    mx = max(mx, len(visited))  # 최대값 재설정
    return # 함수 끝내기
  
  for d in range(2):  # 꺽을지 말지 2상황 탐색
    cov += d # 0, 1 >> 0일때는 꺽지 않고 1일떄는 꺽는다
    if cov > 3:  # 3번 초과로 꺽으면 함수 끝내기
      return
    yy, xx = y+dy[cov], x+dx[cov]   # 현재 위치 이동
    if 0<=yy<n and 0<=xx<n and arr[yy][xx] not in visited: # 현재위치가 좌표평면안에 존재하고 방문한 곳의 디저트가 먹은적이 없다면
      visited.append(arr[yy][xx]) # 디저트를 넣고
      f(yy, xx, cov, visited)   # 현재위치에서 재귀
      visited.pop()     # 디저트 빼기


dy, dx = [1, 1, -1, -1], [1, -1, -1, 1]  # 대각선으로 움직일 방향
T = int(input())
for tc in range(1, T+1):  
  n = int(input())  # 사각형 길이
  arr = [list(map(int, input().split())) for _ in range(n)] # 카페 리스트
  mx = -1  # 방문할 수 있는 최대 개수 변수

  for i in range(n):
    for j in range(n):  # 전체 탐색
      start = [i, j]   # 시작점 설정
      f(i, j, 0, [])   # 시작점, 꺽은 횟수, 디저트종류
  print(f'#{tc} {mx}')