n = int(input())
arr = [3, 5]
cnt1, cnt2 = n//3, n//5
mi = 1000000000
ans = 0
for i in range(cnt1, -1, -1):
  for j in range(cnt2, -1, -1):
    if (i * 3) + (j * 5) == n and i + j < mi:
      ans = i + j
if ans:
  print(ans)
else:
  print(-1)