# def f(start, sum, recur):
#   global cnt
#   if sum == k:
#     cnt += 1
#     return
#   if sum > k or start >= n or recur > maxRecur:
#     return
#   for i in range(start, n):
#     f(start, sum+coin[i], recur+1)
#     start += 1


n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)] # 코인 리스트
dp = [0] * (k+1) # 목표 값까지 경우의 수 받을 리스트
dp[0] = 1 # 모든 동전을 안받을 경우 1

for i in coin: # 동전들의 숫자를 빼기
  for j in range(i, k+1):
    # i의 값은 코인의 가치이다.
    # dp[x] >> 의 의미는 x원이 될 수 있는 경우의 수인데
    # i가 들어가면서 만들 수 있는 경우의 수는 
    # i보다 크거나 같은 숫자만 만들 수 있다.
    # 따라서 j는 i부터 목표 값까지만 경우의 수를 찾으면 된다.
    # dp[j], dp[j-i]는 원래는 i동전을 사용하기 전의 경우의 수이고 i동전을 사용한 경우의 수는
    # dp[j] = dp[j]+dp[j-i] 가 되게 된다.   
    # 예를들어 i 가 5이고 j가 6이면 5동전을 사용해서 할 수 있는 경우의 수는 
    # (5없이 : 1을 만들 수 있는 경우의 수 + 6을 만들 수 있는 경우의 수이다) 
    dp[j] += dp[j-i]
print(dp[-1]) # 목표값은 마지막번쨰이므로 -1출력