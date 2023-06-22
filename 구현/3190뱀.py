from collections import deque
n, k = int(input()), int(input()) # 맵의 크기, 사과 개수
board = [[0] * n for _ in range(n)] # 맵
board[0][0] = -1 # 뱀의 위치 고정
for i in range(k): # 사과 위치 맵에 1로 설정
    y, x = map(int, input().split())
    board[y-1][x-1] = 1

l = int(input()) # 방향 전환 횟수
dir = {} # 방향전환 시간 저장할 딕셔너리
for _ in range(l): # 딕셔너리에 방향전환 시간과 D,L 저장
    a, b = map(str, input().split())
    dir[int(a)] = b

dy , dx = [0,1, 0, -1], [1, 0, -1, 0] # 우 하 좌 상
                                    #   상 우 하 좌 
y, x = 0, 0 # 뱀의 초기 좌표
d, cnt, q = 0, 0, deque() # 뱀의 방향, 시간, 뱀이 있는 위치들 저장할 데크
q.append((0,0)) # 뱀의 초기 좌표 넣기 

while True:
    cnt += 1 # 시간 +1
    yy, xx = y + dy[d], x + dx[d] # 다음 위치 찾기

    if yy<0 or xx<0 or yy>=n or xx>=n : # 범위 벗어나면 그만
        break

    if board[yy][xx] == 0:  # 다음 위치에 아무것도 없으면
        a, b = q.popleft() # 뱀의 꼬리좌표 빼내기
        board[a][b], board[yy][xx] = 0, -1   # 뱀의 꼬리는 없애고 , 머리 좌표는 현재 좌표로 이동
        q.append((yy, xx)) # 뱀의 위치에 현재 위치 추가

    elif board[yy][xx] == 1: # 사과이면 길이가 늘어나니 꼬리 안건드리고 머리길이만 추가
        q.append((yy, xx))
        board[yy][xx] = -1

    else: # 뱀의 몸통을 만나면 끝내기
        break
    y, x = yy, xx # 현재 좌표로 위치 변경
    if cnt in dir and dir[cnt] == 'L': # 만약 방향 전환해야한다면 전환시켜주기
        d = (d-1) % 4
    elif cnt in dir and dir[cnt] == 'D':
        d = (d+1) % 4

print(cnt) 