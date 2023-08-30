from itertools import combinations

def bfs():
    global mx
    li2 = [[0] * m for _ in range(n)]
    for i in range(n):
        li2[i] = li[i].copy()

    visited = [[0] * m for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for k in range(n):
        for l in range(m):
            if li2[k][l] == 2 and visited[k][l] == 0:
                q = [(k, l)]
                while q:
                    y, x = q.pop()
                    for dy, dx in directions:
                        yy, xx = y + dy, x + dx
                        if 0 <= yy < n and 0 <= xx < m and li2[yy][xx] == 0 and visited[k][l] == 0:
                            q.append((yy, xx))
                            visited[yy][xx] = 1
                            li2[yy][xx] = 2

    cnt = sum(row.count(0) for row in li2)
    mx = max(mx, cnt)
    return 


n, m = map(int, input().split())  # 세로 , 가로 길이
li = [list(map(int, input().split())) for _ in range(n)] # 연구소 

empty = [(i, j) for i in range(n) for j in range(m) if li[i][j] == 0]  #비어있는 공간 리스트로 만들기
mx = 0  # 정답 받을 변수

for picks in combinations(empty, 3): # 3개의 벽을 쳐야하니까 비어있는 곳 3개를 선택한 것들 반복
    # print(pick1, pick2, pick3, '픽')
    for pick in picks:  # 3개의 빈공간을 벽으로 만들기
        li[pick[0]][pick[1]] = 1
    bfs()   # bfs탐색
    for pick in picks:  # 벽으로 만든것 다시 빈공간으로 만들기
        li[pick[0]][pick[1]] = 0
print(mx)  # 최대값 출력