xy = [list(map(int, input().split())) for _ in range(3)]
sum1, sum2 = 0, 0 # 신발끈공식 우측 확인용 합, 좌특 확인용 합
for i in range(3): #삼각형이니 3번 더해주기
  sum1 += xy[i][0] * xy[(i+1)%3][1] # 우하 방향으로 곱해서 더해주기
  sum2 += xy[(i+1)%3][0] * xy[i][1] # 좌하 방향으로 곱해서 더해주기

if sum1 == sum2: # 같으면 일직선
  print(0)
elif sum1 > sum2: # sum1이 더크면 반시계
  print(1)
else: # sum2가 더크면 시계
  print(-1)
