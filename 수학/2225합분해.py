n , m = map(int, input().split()) 

dp =[[0] * 201 for _ in range(201)]  # n, m 의 최댓값은 200

for i in range(201): 
  dp[i][1] =1 # m이 1이라면 >> 본인 자신 혼자서만 본인을 만들 수 있기 떄문에 : 경우의 수 1
  dp[i][2] =1+i # m이 2 라면 >> 0~본인 + 본인~0 까지의 경우의 수만 가능하기 떄문에 : 경우의 수 == 본인-0+1 
for i in range(2, m+1):
  dp[1][i] =i # 1을 i개로 만들기 위해서는 i-1개의 0과 1개의 1로 구성가능 : 경우의 수 i개
  for j in range(2, n+1):
    dp[j][i] =(dp[j-1][i] + dp[j][i-1]) % (10**9)
    # 표를 그려서 점화식을 만들어 보면 피보나치 수열 형태로 나옴
print(dp[n][m])
