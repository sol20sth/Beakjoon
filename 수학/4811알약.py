
N = int(input())
for _ in range(N):
    n = int(input())

dp = [[0] * 31 for _ in range(31)]
dp[0] = 1
for i in range(31):
    for j in range(1, i):
        dp[i] += dp[j]
