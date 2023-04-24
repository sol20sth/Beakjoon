def bfs(y, x, maze):
    global stack        # 글로벌 스택
    q = []          # 빈큐
    q.append((y,x))     # 현재 위치 추가
    maze[y][x] = 0      # 현재위치 0으로 바꾸기
    cnt = 1         # 마을개수 셀 변수
    while q:        # 큐가 남아있는동안
        y, x = q.pop(0)     # 큐에서 빼서 현재위치 변경
        for d in range(4):      # 4방향 탐색
            yy = y + dy[d]
            xx = x + dx[d]
            if 0<=xx<n and 0<=yy<n and maze[yy][xx] == 1:       # 범위안에 있고 마을집이 1이면
                q.append((yy,xx))       # 큐에 추가
                maze[yy][xx] = 0        # 방문표시
                cnt += 1                # 집 개수 +1
    stack.append(cnt)               # while 문이 끝났을때 방문한 집 개수를 스택에 추가
    return                      # 함수 끝내기


dy = [-1, 1, 0, 0]      # 방향 움직이기
dx = [0, 0, -1, 1]
n = int(input())
maze = [list(map(int, input())) for _ in range(n)]  # 리스트들 받기
# print(maze)
stack = []  # 마을들의 개수 받을 빈리스트
for i in range(n):
    for j in range(n):          # 전체 탐색 
        if maze[i][j] == 1:     # 1일때 함수발동
            bfs(i, j, maze)

sorted_stack = sorted(stack)      # 스택 정렬
print(len(stack))       # 스택길이 프린트
for i in sorted_stack:  # 스택요소 오름차순으로 프린트
    print(i)

