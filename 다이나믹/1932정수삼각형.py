n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
ans = 0 # 정답 변수
dp = [[[0] for _ in range(i)] for i in range(1, n+1)] # dp리스트 만들기 li랑 똑같은 구조로
# print(dp)

dp[0][0] = li[0][0] # dp꼭지점 꼭지점 값으로 할당

for i in range(1, n): # 2번째줄부터 확인
  for j in range(len(dp[i])): # 각줄의 길이 만큼 dp값찾기
    # print(i, j)
    if j!= 0 and j != len(dp[i])-1: # 좌, 우 끝이 아니면
      dp[i][j] = max(li[i][j] + dp[i-1][j-1], li[i][j] + dp[i-1][j])
      # dp[i][j]의 값은 li의 값과 dp위의 좌우 더해준 값중 큰값
    elif j !=0: # 우측끝이면 좌측만 비교
      dp[i][j] = li[i][j] + dp[i-1][j-1]
    else: #좌측끝이면 우측만 비교
      dp[i][j] = li[i][j] + dp[i-1][j]
# print(dp)
print(max(dp[-1])) # 아래에서 가장 큰값 출력