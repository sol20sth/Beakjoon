n = int(input())

arr =[int(input()) for _ in range(n)]

dp = [0] * 10000000

dp[0] = arr[0]
if n >= 2:
  dp[1] = arr[1] + arr[0]
if n >= 3:
  dp[2] = max(dp[1], arr[1]+arr[2], arr[0]+arr[2])
if n >= 4:
  for i in range(3, n):
    dp[i] = (max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i]))
  # print(dp)
print(max(dp))