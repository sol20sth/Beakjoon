def bfs(time, tomato, arr):
    q = []          # 빈 큐
    mx = 0          # 정답 받을 변수
    q.append(tomato[time])  # 0초의 토마토 리스트 큐에 넣기
    while q:    # 큐가 빌때까지
        time += 1       # 시간늘리고
        for id in q[time-1]:        # 전시간대의 익은 토마토들 꺼내기
            y, x = id               # 좌표 변경
            for d in range(4):      # 4방향 탐생
                yy = y + dy[d]
                xx = x + dx[d]
                if 0<=xx<m and 0<=yy<n and arr[yy][xx] == 0:    # 범위내에 있고 0이면
                    tomato[time].append((yy,xx))    # 이번 시간의 익은 토마토라고 생각하고 좌표 넣기
                    arr[yy][xx] = arr[y][x] + 1     # 시간 추가
        if tomato[time]:        # 이번시간의 익은 토마토가 있으며
            q.append(tomato[time])      # 큐에추가
        else:           # 없으면 종료
            break
    for i in range(n):      # 모든 반복문 종료후 arr 탐색
        for j in range(m):
            if mx < arr[i][j]:  # 최대값 찾기
                mx = arr[i][j]
            elif arr[i][j] == 0:    # 찾는도중 0을 발견하면 -1리턴
                return -1
    return mx  - 1  # 최대값 -1 리턴
            
import sys
input = sys.stdin.readline
dy = [-1, 1, 0, 0]      # 탐색 방향
dx = [0, 0, -1, 1]
m, n = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]    # 토마토 분포리스트
# print(arr)
tomato = [[] for _ in range(n*m+1)] # 익은 토마토 좌표 받기위한 빈 리스트
time = 0        # 시간
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:  # 익은 토마토면 토마토리스트에 좌표 넣기
            tomato[0].append((i,j))
y, x = 0, 0
print(bfs(0, tomato, arr))

