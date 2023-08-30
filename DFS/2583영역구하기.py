def bfs(i, j):
    global y, x
    visited = [[0] * x for _ in range(y)]  # 방문 처리할 리스트
    q = [[i, j]]  # 현재 위치 q에 넣기
    visited[i][j] = 1  # 현재위치 방문처리
    cnt = 1  # 현재위치 방문하였기에 cnt == 1
    while q: # q가 있는동안 반복
        i, j = q.pop()  # 현재위치 i, j 로 설정
        for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 4방향 탐색
            yy, xx = i + d[1], j + d[0]  
            if 0<=yy<y and 0<=xx<x and visited[yy][xx] == 0 and li[yy][xx]==0:
                # 범위내에 존재하며 방문한적없고 직사각형공간이 아니면
                q.append([yy, xx]) # q에 yy, xx위치 추가
                visited[yy][xx] = 1 # 방문처리 
                li[yy][xx] = 1 # 직사각형공간으로 처리
                cnt += 1  # 개수 +1
    return cnt

y, x , n = map(int, input().split())  # y, x, n : y길이 , x길이 , 직사각형 갯수
li = [[0] * x for _ in range(y)]  # 2차원 빈 리스트

for _ in range(n):  # 직사각형 개수만큼 반복 후 채우기
    x1, y1, x2, y2 = map(int, input().split())  # x, y좌표 2개 받아서 변수처리
    for i in range(min(y1, y2), max(y1, y2)):  # 직사각형의 공간을 1로 채우기
        for j in range(min(x1, x2), max(x1, x2)):
            li[i][j] = 1
ans = []  # 정답받을 리스트
for i in range(y-1, -1, -1):  # 위아래 바뀌어서 반대로 반복
    for j in range(x-1, -1, -1):
        if li[i][j] == 0:  # 직사각형 공간이 아니면
            tmp = bfs(i, j)  # 함수 실행
            ans.append(tmp)  # 정답에 tmp넣기
ans = sorted(ans) # 정렬 
print(len(ans))   # 영역 개수
for i in ans:    # 영역의 남는공간 넓이 하나씩 출력
    print(i, end=" ")


