import sys
input = sys.stdin.readline

def bfs(x, y, visited):
    visited[x][y] = 1 
    q = []
    q.append((x, y))    # q에 현재 위치 추가
    while q:    # q 가 있다면
        x, y = q.pop(0)   # q에서 빼서 위치 변경
        for dx, dy in xy: # 방향 탐색
            yy = y + dy
            xx = x + dx
            # 범위내에 있고 같지 않고 방문한적이 없으면
            if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] == arr[x][y] and not visited[xx][yy]:
                    visited[xx][yy] = 1   # 방문표시
                    q.append((xx, yy))    # 큐에 추가
                    
                    
xy = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 방향설정
n = int(input())
arr = [list(map(str, input().strip())) for _ in range(n)] #글자들
visited = [[0] * n for _ in range(n)] # 적록색약이 아닌사람이봤을떄
visited2 = [[0] * n for _ in range(n)]  #석록색약인 사람이 봤을때
cnt = 0   #1번케이스 정답변수
cnt2 = 0  #2번 케이스 정답변수

for i in range(n):
    for j in range(n):
        if not visited[i][j]: # 1번케이스 전체 탐색 
            bfs(i, j, visited)  # 같은 구간들 모두 방문표시
            cnt += 1      # 한구간 끝나면 +1

for i in range(n):    # 2번케이스 찾기 위해 R을 G로 변경
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

for i in range(n):    # 1번 케이스처럼 똑같이 함수 실행
    for j in range(n):
        if not visited2[i][j]:
            bfs(i, j, visited2)
            cnt2 += 1
print(cnt, end=' ')            
print(cnt2)