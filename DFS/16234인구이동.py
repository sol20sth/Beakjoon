def checkMap(y, x): # 리스트 내에 있는지 확인 함수
    if 0<=y<n and 0<=x<n:
        return True
    return False

def bfs(y, x):  # bfs 탐색 
    global country  
    q = deque()  # 좌표 저장할 deque
    q2 = []  # 방문한 위치 저장할 스택
    q.append((y, x)) # 현재위치 q, q2에 저장
    q2.append((y, x))
    visited[y][x] = 1 # 현재 위치 방문처리
    while q:  # q가 남아있는동안 반복
        y, x = q.popleft() # 현재 위치 재설정
        for d in range(4):  # 4방향 탐색
            yy, xx = y + dy[d], x + dx[d] 
            if checkMap(yy,xx) and visited[yy][xx]==0 and l<=abs(country[yy][xx]-country[y][x])<=r:
                # 리스트 내에 있고 방문한적 없고 인구 차이가 범위내에 있으면
                q.append((yy, xx))  # q, q2에 저장
                q2.append((yy, xx))
                visited[yy][xx] = 1 # 방문처리
    return q2  # 방문한 리스트 리턴
        
import sys
from collections import deque
input = sys.stdin.readline
n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
# 인구 리스트
ans = 0 # 정답 받을 변수
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

while True:
    ans += 1 # 인구이동 1번당 +1
    visited = [[0] * n for _ in range(n)] # 인구이동할떄마다 새로운 방문리스트 필요함
    TF = False  # 인구이동 필요한지 없는지 확인 변수
    for i in range(n): # 전체 탐색
        for j in range(n):
            if visited[i][j] == 0: # 방문한 적 없으면
                tmp = bfs(i, j) # bfs 탐색 후 방문한 곳 리스트 tmp에 담기
                if len(tmp) > 1: # 연합이 생기면
                    TF = True # 인구이동 해야함
                    sm = 0 # 연합인구합 받을 변수
                    for y, x in tmp:  # 인구합 구하기
                        sm += country[y][x]
                    sm = sm//len(tmp) # 길이로 나누기
                    for y, x in tmp:  # 이동 한 곳들 인구리스트에 재할당
                        country[y][x] = sm
    if TF ==False: # 더이상 인구이동이 필요하지 않으면
        print(ans-1)  # 인구이동 한 수 만큼 출력
        break # 반복문 종료