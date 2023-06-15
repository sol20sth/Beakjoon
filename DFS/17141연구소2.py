from collections import deque
from itertools import combinations

dr = [0,1,0,-1]
dc = [1,0,-1,0]
N,M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

#벽
wall = []
#바이러스 후보 
virus_sub = []

for r in range(N) :
    for c in range(N) :
        if grid[r][c] == 1 :
            wall.append((r,c))
        #바이러스 후보에 추가 후 통로로 변경 
        elif grid[r][c] == 2 :
            virus_sub.append((r,c))
            grid[r][c] = 0

#정답 초기 값 
res = 10e9
#M개만큼 바이러스로 설정하고 
for virus in combinations(virus_sub,M) :
    #방문배열 만들기 
    visited = [[0]*N for _ in range(N)]
    #큐에 넣기 
    v = deque(virus[:])
    #바이러스는 선언하고 방문처리 
    for r,c in virus :
        grid[r][c] = 2 
        visited[r][c] = 1
    #종료조건을 만들 cnt는 바이러스수 + 벽의 수 
    cnt = M+len(wall)
    while v :
        cr,cc = v.popleft()

        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d]
            #네방향 돌면서 한걸음 추가하고 cnt도 추가 
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and grid[nr][nc] == 0 :
                visited[nr][nc] = visited[cr][cc] + 1 
                v.append((nr,nc))
                cnt += 1 
            #맵이 다 바이러스가 되면 
            #최소값 갱신 
            if N**2 - cnt == 0:
                tmp = 0
                for r in range(N) :
                    tmp = max(max(visited[r]),tmp)
                
                if tmp<res :
                    res = tmp 
                break
    #다시 통로로 만들어주기 
    for r,c in virus :
        grid[r][c] = 0

if res>=10e9 :
    print(-1)
else :
    print(res-1)