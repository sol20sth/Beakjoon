import sys
input = sys.stdin.readline

n,m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
move = [[x[0] - 1, x[1]] for _ in range(m) for x in [list(map(int, input().split()))]]
# 움직이는 방향 , 거리 저장할 리스트
clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]] # 처음 구름 설정
dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 구름이동 방향
dy = [0, -1, -1, -1, 0, 1, 1, 1]
for d, s in move: # move에서 하나씩빼서 방향, 거리 
    movedcloud = [] # 움직인 구름 위치 저장
    visited = [[0]*n for _ in range(n)] # 이동 완료한 구름 위치 방문리스트
    for cloud in clouds: # 구름들 옮기기
        yy = (cloud[0] + dy[d]* s) % n  # (원래좌표 + 방향 * 거리 ) % n 좌표평면이 이어져있기 때문  
        xx = (cloud[1] + dx[d]* s) % n
        movedcloud.append([yy,xx]) # 다음 구름좌표에 넣기
        visited[yy][xx] = 1  # 움직였으니 다음 구름은 생성x하기 위해서 방문처리 
        li[yy][xx] += 1  # 구름위치 바구니 +1

    clouds = [] # 구름 없어짐

    dy2 = [-1,-1,1,1] # 4대각선 방향 탐색
    dx2 = [-1,1,-1,1]
    for y,x in movedcloud:  # 이동완료한 구름위치에서 4방향 탐색 후 물이있으면 +1
        cnt = 0
        for i in range(4):
            yy = y+ dx2[i]
            xx = x+ dy2[i]
            if 0<= yy <n and 0<= xx <n and li[yy][xx]: 
                cnt += 1
        li[y][x] += cnt

    for i in range(n):  # 다음 구름 위치 찾아서 cloud에 넣어주기
        for j in range(n):
            if li[i][j] >= 2 and visited[i][j] == 0:
                li[i][j] -= 2
                clouds.append([i,j])
ans = 0
for i in range(n):  # 다끝나면 다 더해주기
    ans += sum(li[i])
print(ans)