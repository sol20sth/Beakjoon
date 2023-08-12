from collections import deque

def bfs(p):  
    dy = [0, 0, -1, 1]  # y, x축 이동 할 방향 만들기
    dx = [-1, 1, 0, 0]  
    start = []  # 사람위치 저장할 리스트
    
    for i in range(5): 
        for j in range(5):
            if p[i][j] == 'P':  # 사람위치 저장하기
                start.append([i, j])
    for s in start:   # 각각의 사람에서 모두 탐색
        queue = deque([s])  
        visited = [[0]*5 for _ in range(5)] # 방문했는지 안했는지 탐색리스트   
        visited[s[0]][s[1]] = 1     # 현재위치 방문 처리
        while queue:  # q가 있는동안 실행
            y, x = queue.popleft()   # 현재 위치 q에서 빼내서 이동
            for d in range(4):  # 4방향탐생
                yy = y + dy[d]
                xx = x + dx[d]
                if 0<=yy<5 and 0<=xx<5 and visited[yy][xx] == 0: # 리스트 범위내에 있으며 방문한 적없으면
                    if p[yy][xx] == 'O':  # 빈테이블 일때 
                        queue.append([yy, xx])  # 위치 저장
                        visited[yy][xx] = visited[y][x] + 1  # 방문처리 후 +1만큼 거리라고 표시 
                    if p[yy][xx] == 'P' and visited[y][x] <= 2:  # 사람이면 거리 3일때 2이니 2이하이면 0 리턴
                        return 0
    return 1  # 모든 판별 만족하면 1리턴

def solution(places):
    answer = []
    for i in range(5):
        answer.append(bfs(places[i]))  # 5가지 경우 모두 bfs탐색 후 넣기
    
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))