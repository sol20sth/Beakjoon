import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]      # 현재위치에서 탐색할 위치 옮길 방법
dy = [0, 0, -1, 1]
def findb(x,y):
    stack = [(x,y)]     # 스택에 현재 위치 추가해놓기
    arr[x][y] = 0       # 현재 위치 0으로 바꿔주기
    while stack:        # 스택이 비어있을떄 그만두기
        x, y = stack.pop()     # 스택에서 빼서 현재위치 이동
        for d in range(4):
            xx = x + dx[d]      # 한칸씩움직이는데
            yy = y + dy[d]
            if 0<= xx <= m-1 and 0<= yy <= n-1 and arr[xx][yy] ==1:     # 그래프안에 있으며 값이 1이면 
                stack.append((xx, yy))      # 스택에 위치 추가 
                arr[xx][yy] = 0         # 0으로 바꿔주기
        else:
            if not stack:       # 더이상 돌아갈 곳이 없으며 인접한 곳들이 모두 0 이되면 함수 종료 >>>>> 이렇게 모든 점
                break           # 들을 탐색해서 1들이 인접한 것들을 모두 없애주기
        
            
T = int(input())

for tc in range(T):
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]   # 세로 m 가로 n인 빈리스트
    # print(arr)
    for i in range(k):      # 배추들이 있는 위치 1로 만들기
        x, y = map(int, input().split())
        arr[x][y] = 1
    cnt = 0         # 정답 구하기위한 카운트
    for i in range(m):          # 행렬 탐색해서 1일때 마다 함수를 돌려줘서 인접한 1들을 모두 없애줄 예정
        for j in range(n):
            if arr[i][j] == 1:  # 1이면 
                findb(i,j)      # 함수를 호출
                cnt += 1        # 한번 호출하면 1추가
    print(cnt)

