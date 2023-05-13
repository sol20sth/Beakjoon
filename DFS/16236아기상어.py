def find_children():        # 아기상어 위치 찾는 함수
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9: # 리스트에 9찾으면 좌표 리턴
                return (i, j) 

def check_line(y, x):  # y, x 가 리스트 범위내에 있는지 확인하는 함수
    if 0<=y<n and 0<=x<n:
        return True # 리스트 내에 있으면 True
    return False # 없으면 False

def bfs(sea, q, visited): # 바다리스트, 스택q, 방문처리 리스트 담고 bfs
    global ans  # 정답받기위한 변수
    cnt, size = 0, 2 # 먹은 횟수 변수, 사이즈 변수
    while q:  # q가 있는동안 돌기
        q.sort(key=lambda x : (x[2], x[0], x[1]))
        # 스택 정렬 >> 거리, y축좌표, x축좌표 순으로 정렬
        y, x, dis = q.pop(0) # y, x, dis = y, x, 거리 변수 뽑아내기
        if sea[y][x] > size: # 물고기 크기가 상어보다 크다면 continue
            continue
        elif sea[y][x] < size: # 물고기 크기가 상어보다 작다면
            if sea[y][x] != 0: # 물고기가 있다면
                q = []   # 현재 좌표로 q, visited 초기화 시키고 현재 좌표로 재시작 하기 위한 준비
                q.append((y, x, 0)) # 빈스택에 y, x, 거리 추가
                ans += visited[y][x] - 1 # 정답에 거리 더해주기
                
                visited = [[0]*n for _ in range(n)] # 방문처리리스트도 초기화
                visited[y][x] = 1 # 현재좌표 방문처리
                cnt += 1  # 먹었으니까 먹은 횟수 +1
                if cnt == size: # 만약 사이즈가 먹은 횟수 == 사이즈이면
                    size += 1 # 사이즈 +1 키우기
                    cnt = 0 # 먹은 횟수 으로 초기화
                sea[y][x] = 0 # 현재위치 물고기 없애기
                continue
            else: # 물고기가 없고 바다라면
                for d in range(4):  # 4방향 탐색 후 
                    yy, xx = y + dy[d], x + dx[d]
                    if check_line(yy, xx):  # 바다리스트내에 있으면
                        if visited[yy][xx] == 0: # 방문한적 없으면
                            q.append((yy, xx, dis+1)) # y, x, 거리 +1  스택에 추가
                            visited[yy][xx] = visited[y][x]+1 # 방문처리 현재 거리에서 +1
        else: # 물고기가 상어와 크기가 같다면
            for d in range(4):  # 통과만 할거니까 4방향 탐색
                yy, xx = y + dy[d], x + dx[d]
                if check_line(yy, xx): # 범위내에 있으면
                    if visited[yy][xx] == 0: # 방문한 적 없으면
                        q.append((yy, xx, dis+1))  # 통과하기 위해 스택에 추가
                        visited[yy][xx] = visited[y][x]+1  # 방문처리

dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]  # 방향탐색 위좌우아래
n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)] # 바다 리스트
(y, x) = find_children()  # 상어 위치
ans = 0 # 정답받을 리스트
q = [] # 빈 스택
q.append((y, x, 0))  # 현재위치와 , 상어와의 거리
visited = [[0] * n for _ in range(n)] # 방문처리 할 리스트
visited[y][x] = 1 # 현재 상어위치 방문처리
sea[y][x] = 0 # 현재 상어위치 0으로 바꾸기
bfs(sea, q, visited)  # 함수 실행
print(ans) # 정답 출력

