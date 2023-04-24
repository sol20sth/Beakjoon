import sys
input = sys.stdin.readline


dx = [1, 1, 1, 0, 0, -1, -1, -1]    # 움직일 위치 방향 정하기
dy = [1, 0, -1, 1, -1, 1, 0, -1]

def go(i,j):        # 움직이는 함수 i, j  >> 현재위치
    arr[i][j] = 0   # 도착하면 방문처리
    for d in range(8):  # 대각포함 8방향으로 다확인
        dj = j + dx[d]
        di = i + dy[d]
        if 0<=dj<w and 0<=di<h and arr[di][dj] == 1:    # 범위내에 있고 1일때
            go(di, dj)      # 인접해있는 1인 부분들을 계속찾아서 0으로 만들기

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:   # 0,0 이입력되면 끝내기
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    if arr == [[0]*w for _ in range(h)]:    # 리스트가 비어있으면 값을 출력하고 계속 while문 반복
        print(ans)
        continue
    for i in range(h):      # 전체 구간 확인
        for j in range(w):
            if arr[i][j]==1:    # 값이 1일때
                ans += 1    # 섬1개 추가
                go(i,j)     # 근접해있는 땅들을 하나의 섬으로 인식하기위해 함수발동

    print(ans)
                
                    