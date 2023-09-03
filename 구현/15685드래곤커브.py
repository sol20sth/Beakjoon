dy, dx = [0, -1, 0, 1], [1, 0, -1, 0] # 우 상 좌 하 

n = int(input())
li = [[0 for _ in range(101)] for _ in range(101)] # 최대 101칸씩 0~101

def f(x, y, d, time):
  global li
  li[y][x] = 1  # 현재위치 방문처리
  curve = [d]  # 커브 리스트에 처음 방향 넣기
  for j in range(time): # time만큼 반복
      for k in range(len(curve) - 1, -1, -1): # time기준으로 curve의 리스트전체를 90도 회전한 방향을 집어넣기
          curve.append((curve[k] + 1) % 4)

  for j in range(len(curve)): # 한칸씩 이동시키며 해당 위치 1처리
      y += dy[curve[j]]
      x += dx[curve[j]]
      li[y][x] = 1
  return 

for i in range(n):  # n만큼 받아서 정답찾기
  x, y, d, time = map(int, input().split())
  f(x, y, d, time)

cnt = 0
for i in range(100): # 최대 100칸이니 99칸까지 탐색 정사각형 찾기위해
  for j in range(100):
    if li[i][j] == 1 and li[i+1][j] == 1 and li[i][j+1] == 1 and li[i+1][j+1] == 1 :
      # 정사각형 판별 조건문
      cnt += 1  # 꼭지점 모두 1이면 cnt +=1
print(cnt)
